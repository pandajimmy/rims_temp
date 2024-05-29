from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.core import serializers
import requests
import json
import uuid
import calendar
from _lib import panda
from _lib import rims_data_functions
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status,viewsets
from collections import defaultdict
from django.http import QueryDict
import pprint
from django.http import JsonResponse 
from django.core.serializers.json import DjangoJSONEncoder   
from datetime import date
from datetime import datetime
from datetime import timedelta

from decimal import Decimal 

from django.db import connection 


from _mc_tta_list.models import TtaList
from _mc_tta_list_purchase_n_rebates.serializers import TtaListPurchaseNRebatesSerializer
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from _ml_rims_brand.models import RimsBrand
from _ml_rims_supcus.models import RimsSupcus
from _ts_tta_cal_log.models import TtaListCalLogs
from _ts_tta_cal_log.serializers import TtaListCalLogsSerializer 
from _ts_tta_invmain.models import TtaInvmain
from _ts_tta_invmain.serializers import TtaInvmainSerializer 
from _ts_tta_invchild.models import TtaInvchild
from _ts_tta_invchild.serializers import TtaInvchildSerializer
from _mc_tta_list_purchase_n_rebates.models import TtaListPurchaseNRebates
from _mc_get_customer_profile.models import CustomerProfile


def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) +  timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - timedelta(days=next_month.day)

def daterange_condition(label , cal_date, var_date_from, var_date_to):
    # print(label)
    # print(cal_date)
    # panda.check_type(cal_date)
    # print('========')
    ps_from = datetime.strptime(var_date_from,'%Y-%m-%d')
    ps_to = datetime.strptime(var_date_to,'%Y-%m-%d')
    # print(ps['label'])
    # print('ps_from')
    # print(ps_from)
    # panda.check_type(ps_from)
    # print('*********')
    
    # if (cal_date >= ps_from) and (cal_date <= ps_to):
    #     #caldate = 2022-08-30
    #     #2022-01-01 <= 2022-08-30 <= 2022-08-31
    #     datefrom1 = cal_date.replace(day=1).strftime('%Y-%m-%d')
    #     #dateto1 = str(last_day_of_month(datetime.date(cal_date)))
    #     dateto1 = cal_date
    #     # cond = '1'
        
    # elif (cal_date >= ps_from )and (cal_date >= ps_to): 
    #     #caldate = 2022-08-30
    #     #2022-08-30  >= 2022-01-01 && 2022-08-30 >= 2022-01-31
    #     datefrom1 = '2099-12-01'
    #     dateto1 =  '2099-12-31'  
    #     # cond = '2'
        
    # elif (cal_date <= ps_from) and (cal_date <= ps_to):
    #     #caldate = 2022-08-30
    #     #2022-09-01  >= 2022-08-30 && 2022-09-31 >= 2022-08-30
    #     datefrom1 = '2099-12-01'
    #     dateto1 =  '2099-12-31'  
    #     # cond = '3'
    # else:
    #     datefrom1 = '2099-12-01'
    #     dateto1 =  '2099-12-31'  
    #     # cond = '4'

    if (cal_date >= ps_from) and (cal_date <= ps_to):
        #caldate = 2022-08-30
        #2022-01-01 <= 2022-08-30 <= 2022-08-31
        datefrom1 = cal_date.replace(day=1).strftime('%Y-%m-%d')
        #dateto1 = str(last_day_of_month(datetime.date(cal_date)))
        dateto1 = cal_date.strftime('%Y-%m-%d')
        # cond = '1'
        
    else : 
        #caldate = 2022-08-30
        #2022-08-30  >= 2022-01-01 && 2022-08-30 >= 2022-01-31
        datefrom1 = '2099-12-01'
        dateto1 =  '2099-12-31'  
        # cond = '2' 



    # print(ps['label'])
    # print('ps_to')
    # print(ps_to)
    # panda.check_type(ps_to)
    # print(cond)
    # print('========') 
    return  {'label': label, 'cal_date': cal_date, 'date_from': datefrom1 , 'date_to': dateto1}


#create data into inv child and header
def create_inv_header_child(data, customer_guid, result, calval_method):
                            if(calval_method == 'non_tier'):
                                if(result['value'] != 0):
                                    if(data['prefix1'] == '%'): 
                                        cal_val = round((float(data['bf_amount'])*float(result['value']))/100,2)
                                    else:
                                        cal_val = data['bf_amount']
                                else:
                                    cal_val = 0      
                            elif(calval_method == 'tier'): 
                                # print(result['rebate'])
                                cal_val = 1
                                #cal_val = result['rebate']['tierPurchaseAmt'] 
                                
                            else:
                                cal_val = result['value'] 


                            #print(result['value'])
                            #check invmain exist
                            #insert main 
                            try: 
                                check_invmain_exist = TtaInvmain.objects.get(docno=data['refno'], customer_guid=data['customer_guid']) 
                                #print('#############################',data['refno'])
                            except TtaInvmain.DoesNotExist:
                                check_invmain_exist = TtaInvmain(docno=data['refno']
                                        , customer_guid=data['customer_guid']
                                        , invoice_date=date.today()
                                        , code=data['code']
                                        , name=data['name']
                                        , created_by='system'
                                        , updated_by='system'
                                        )
                                check_invmain_exist.save()   

                                

                                #update_profile = TtaList.objects.get(refno=data['refno'], customer_guid=data['customer_guid'])  
                                update_profile = TtaList.objects.filter(refno=data['refno']).filter(customer_guid=data['customer_guid']).values_list('supplier_profile', flat=True)
                                
                                get_data = update_profile[0]
                                for data1 in get_data:
                                    if data1['field'] == "bill_supp_name":
                                        option_value = data1['prefix1']['options']
                                        
                                    if data1['field'] == "supplier_pic":
                                        pic = data1['input1']
                                
                                        
                                for opt_val in option_value:
                                    add1 = opt_val['add1']
                                    add2 = opt_val['add2']
                                    add3 = opt_val['add3']
                                    add4 = opt_val['add4']
                                    term = opt_val['term']
                                    
                                
                                TtaInvmain.objects.filter(docno=data['refno'], customer_guid=data['customer_guid']).update(
                                    add_1=add1
                                    , add_2=add2
                                    , add_3=add3
                                    , add_4=add4
                                    , term=term 
                                    , attn=pic
                                    )
                                                            
                            get_invmainguid = TtaInvmain.objects.get(docno=data['refno'], customer_guid=data['customer_guid']) 

                            if cal_val != 0:   
                                if calval_method == 'tier':
                                    #insert child tier
                                    for t_loop in result['rebate']: 
                                        #print(t_loop['rebateValue'])
                                        t = 1
                                        if t_loop['rebateValue'] != 0: 
                                            
                                            query_line = TtaInvchild.objects.filter(invmain_guid=get_invmainguid, customer_guid=data['customer_guid'])
                                            
                                            line = query_line.count() + 1  
                                            check_invchild_exist = TtaInvchild(
                                                customer_guid=data['customer_guid']
                                                , invmain_guid=get_invmainguid
                                                , line=line
                                                , description=data['label'] + str(t)
                                                , pricetype=data['prefix1']
                                                , unit_price=data['bf_amount']
                                                , qty='1'
                                                , totalprice=t_loop['rebateValue']
                                                , total_incl_tax=t_loop['rebateValue']
                                                , created_by='system'
                                                , updated_by='system'
                                                ) 
                                            check_invchild_exist.save() 
                                            t = t+1 
                                else:
                                    #insert child   
                                    query_line = TtaInvchild.objects.filter(invmain_guid=get_invmainguid, customer_guid=data['customer_guid'])
                                    
                                    line = query_line.count() + 1  
                                    check_invchild_exist = TtaInvchild(
                                        customer_guid=customer_guid
                                        , invmain_guid=get_invmainguid
                                        , line=line
                                        , description=data['label']
                                        , pricetype=data['prefix1']
                                        , unit_price=data['bf_amount']
                                        , qty='1'
                                        , totalprice=cal_val
                                        , total_incl_tax=cal_val
                                        , created_by='system'
                                        , updated_by='system'
                                        ) 
                                    check_invchild_exist.save() 
                
                            
                            #result_status = posting_status["status"]
                            return result
                            #return Response({"status":"true","result":connection.queries}) 


def error_log(list_guid, customer_guid, log_module, data, result):
        
        log = TtaListCalLogs(
                    log_guid=panda.panda_uuid()
                    , customer_guid=customer_guid
                    , list_guid=list_guid
                    , log_module=log_module
                    , log_ref=data['label']
                    , log_json = data
                    , remark = result
                    )  
        log.save()  


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def tta_vendor(request):
    if request.method == 'POST':  
        request_data = QueryDict.dict(request.data) 
        customer_guid = str(request_data['customer_guid'])
        consolidate_result = []

        result_1 = TtaList.objects.filter(customer_guid=customer_guid).values('list_guid','supplier_profile')
        
        force_new_dict = {}

        final_list =[]

        for result  in result_1: 

            for sp in result['supplier_profile']:

                force_new_dict['list_guid'] = result['list_guid'] 

                if sp['field'] == 'supplier_name': 
                    #supcus_guid = sp['prefix1']['value'] 
                    val_supplier_guid = sp['prefix1']['value']
                    if type(val_supplier_guid) == str: 
                            val_supplier_guid = list(val_supplier_guid.split(" "))  

                    q_supcode = RimsSupcus.objects.filter(supcus_guid__in=val_supplier_guid).filter(customer_guid=customer_guid).values_list('code', flat=True)
                    supcode = list(q_supcode) 
                    sup_guid = val_supplier_guid 
                    force_new_dict['supcode'] = supcode
                    force_new_dict['sup_guid'] = val_supplier_guid 
                    
                    tobecopy = force_new_dict

                    final = tobecopy.copy()
                    final_list.append(final)  
    
        return Response({"status":"true","result":final_list}) 
        #return Response({"status":"true","result":outlet}) 
    else:
        return HttpResponse("Invalid Method")


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def check_tta(request):
    if request.method == 'POST':  
        request_data = QueryDict.dict(request.data) 
        customer_guid = str(request_data['customer_guid'])
        list_guid_array = request_data['list_guid']
        
        cal_date = datetime.strptime(request_data['cal_date'],'%Y-%m-%d')
        
        #get_TtaListCalLogs = TtaListCalLogs.objects.all()

        consolidate_result = []
        tier_result = {}
        dicts = [] 

        live_mode = True 

        #loop through  list_guid that need to undergo data processing
        for list_guid in list_guid_array:   
            result_1 = TtaList.objects.get(customer_guid=customer_guid, list_guid=list_guid)  
            consolidate_result.append(result_1)   
        
        #tta check_datefrom_dateto 
        tta_period_from = datetime.strptime(consolidate_result[0].tta_period_from,'%Y-%m-%d')
        tta_period_to = datetime.strptime(consolidate_result[0].tta_period_to,'%Y-%m-%d')

        if tta_period_from <= cal_date <= tta_period_to:
            datefrom = cal_date.replace(day=1).strftime('%Y-%m-%d')
            #dateto = str(last_day_of_month(datetime.date(cal_date)).strftime('%Y-%m-%d')) 
            dateto =  last_day_of_month(datetime.date(cal_date)).strftime('%Y-%m-%d')
        # elif tta_period_to <= cal_date : 
        #     datefrom =  cal_date.replace(day=1).strftime('%Y-%m-%d')
        #     dateto = str(tta_period_to).strftime('%Y-%m-%d') 
        else:
            datefrom = '2099-12-01'
            dateto =  '2099-12-31'  

            return Response({"status":"true","result":list_guid_array})
            # return Response({"status":"true","result":'Bypass Date Out of Range'})
        
        # Extract individual columns from the request
        supplier_guid = request.POST.get('supplier_guid')
        supplier_name = request.POST.get('supplier_name')
        outlet1 = request.POST.get('outlet1')
        outlet2 = request.POST.get('outlet2')

        # Process each field individually using the extracted values
        if outlet1 == "All":
            q_outlet = RimsCpSetBranch.objects.exclude(set_active=0).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        elif outlet1 == "Outlet" and outlet2:
            val_outlet = outlet2.split(',')
            q_outlet = RimsCpSetBranch.objects.filter(branch_guid__in=val_outlet).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        else:
            outlet = []  # Default value when conditions don't match

        exclude_outlets = request.POST.getlist('exclude_outlet[]')  # Assuming 'exclude_outlet' is an array in the POST data
        excluded_branch_guids = []

        for exclude_outlet in exclude_outlets:
            excluded_branch_guids.append(exclude_outlet['branch']['branch_guid'])

        q_outlet = RimsCpSetBranch.objects.exclude(set_active=0).exclude(branch_guid__in=excluded_branch_guids).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
        outlet = list(q_outlet) 

        trading_brands = request.POST.getlist('trading_brand[]')  # Assuming 'trading_brand' is an array in the POST data
        brands = []  # Initialize an empty list to store the brand codes
        for trading_brand in trading_brands:
            brand_guid = trading_brand['brand']['brand_guid']
            q_brand = RimsBrand.objects.filter(brand_guid=brand_guid, customer_guid=customer_guid).values_list('code', flat=True)
            brands.extend(q_brand) 

        # Process 'supplier_name' field
        if supplier_name:
            val_supplier_guid = supplier_guid.split()
            q_supcode = RimsSupcus.objects.filter(supcus_guid__in=val_supplier_guid).filter(customer_guid=customer_guid).values_list('code', flat=True)
            supcode = list(q_supcode)

        for result_1 in consolidate_result:
            purchase_n_rebates = result_1.purchase_n_rebates
            payment_n_discount = result_1.payment_n_discount
            stock_n_deliveries = result_1.stock_n_deliveries
            administration_fees = result_1.administration_fees
            supcode = result_1.bill_supp_code
        
        # Purchase_n_rebates 
        purchase_list = []

        for list_guid in list_guid_array:
            result_1 = TtaList.objects.get(customer_guid=customer_guid, list_guid=list_guid)
            purchase_list.append(result_1.purchase_n_rebates)

        print(purchase_list)

        for purchase in purchase_list:
            for rebate_key, rebate_value in purchase.__dict__.items():
                # Skip non-rebate fields and fields with zero value
                if rebate_key.endswith('_value') and rebate_value > 0.0:
                    rebate_type_key = rebate_key.replace('_value', '_type')
                    rebate_type_value = getattr(purchase, rebate_type_key)
                    rebate_value_type_key = rebate_key.replace('_value', '_value_type')
                    rebate_value_type_value = getattr(purchase, rebate_value_type_key)

                    print("Rebate Value: ", rebate_value)
                    print("Rebate Type Key: ", rebate_type_key)
                    print("Rebate Type Value: ", rebate_type_value)
                    print("Rebate Value Type Key: ", rebate_value_type_key)
                    print("Rebate Value Type Value: ", rebate_value_type_value)

                    if rebate_value_type_value in ['GPV', 'NPV', 'Monthly', 'Yearly']:
                        q_type = 'gr_gross_sum' if rebate_value_type_value == 'GPV' else 'gr_net_sum' if rebate_value_type_value == 'NPV' else 'Monthly' if rebate_value_type_value == 'Monthly' else 'Yearly'

                    label = rebate_key.replace('_value', '').replace('_', ' ').title()

                    print("Q Type: ", q_type)
                    print("Label: ", label)

                    data = {
                        "customer_guid": customer_guid,
                        "refno": result_1.refno,
                        "code": result_1.supplier_code,
                        "name": result_1.supplier_name,
                        "prefix1": rebate_type_value,
                        "type": q_type,
                        "label": label,
                        "startDate": datefrom,
                        "endDate": dateto,
                        "outlet": outlet,
                        "brand": brands,
                        "supcode": supcode,
                        "bf_amount": rebate_value,
                        "rebate_method": [
                            {
                                "range": Decimal(0.00),
                                "type": '%',
                                "value": Decimal(0.00)
                            }
                        ]
                    }

                    print("Customer GUID: ", customer_guid)
                    print("Ref No.: ", result_1.refno)
                    print("Supplier Code: ", result_1.supplier_code)
                    print("Supplier Name: ", result_1.supplier_name)
                    print("SupCode: ", supcode)
                    print("Outlet: ", outlet)
                    print("Start Date: ", datefrom)
                    print("End Date: ", dateto)

                    result = rims_data_functions.gr_sum(data)
                    if result['status'] == live_mode:
                        calval_method = 'non_tier'
                        add_data = create_inv_header_child(data, result, calval_method)
                    else:
                        error_log(list_guid, 'check_tta', data, result)

    
        #payment_n_discount
        for discount_key, discount_value in payment_n_discount.items():
            # Skip non-discount fields and fields with zero value
            if discount_key.endswith('_value') and discount_value > 0:
                discount_type_key = discount_key.replace('_value', '_type')
                discount_type_value = payment_n_discount[discount_type_key]

                q_type = 'Yearly'  # Default type, change as necessary

                if discount_type_value in ['GPV', 'NPV', 'Monthly', 'Yearly']:
                    q_type = 'gr_gross_sum' if discount_type_value == 'GPV' else 'gr_net_sum' if discount_type_value == 'NPV' else 'Monthly' if discount_type_value == 'Monthly' else 'Yearly'

                label = discount_key.replace('_value', '').replace('_', ' ').title()

                data = {
                    "customer_guid": customer_guid,
                    "refno": result_1.refno,
                    "code": result_1.supplier_code,
                    "name": result_1.supplier_name,
                    "prefix1": discount_type_value,
                    "type": q_type,
                    "label": label,
                    "startDate": datefrom,
                    "endDate": dateto,
                    "outlet": outlet,
                    "brand": brands,
                    "supcode": supcode,
                    "bf_amount": discount_value,
                    "rebate_method": [
                        {
                            "range": Decimal(0.00),
                            "type": '%',
                            "value": Decimal(0.00)
                        }
                    ]
                }

                result = rims_data_functions.gr_sum(data)
                if result['status'] == live_mode:
                    calval_method = 'non_tier'
                    add_data = create_inv_header_child(data, result, calval_method)
                else:
                    error_log(list_guid, 'check_tta', data, result)

        #stock_n_deliveries 
        query_snd = consolidate_result[0].stock_n_deliveries 
        for snd in query_snd:
            try:   
                if(snd['calMethod'] == 'Method1') and (snd['input1'] > '0.00'):  
                    if snd['radio1']['value'] == 'GPV':
                        q_type = 'gr_gross_sum'
                    elif  snd['radio1']['value'] == 'NPV':
                        q_type = 'gr_net_sum'
                    elif  snd['radio1']['value'] == 'Monthly':
                        q_type = 'Monthly'
                    elif  snd['radio1']['value'] == 'Yearly':
                        q_type = 'Yearly'            
                    else:
                        q_type = 'unknown'
                    
                    field = snd['field']
                    label = snd['label']
                    input1 = snd['input1']
                    radio = snd['radio1']['value']
                    prefix1 = snd['prefix1']['value']

                    calmethod = 'sum_method'

                    if calmethod == 'sum_method': 
                        data = {
                            "customer_guid":customer_guid, 
                            "refno":result_1.refno, 
                            "code":result_1.supplier_code, 
                            "name":result_1.supplier_name, 
                            "prefix1": prefix1,
                            "type":q_type,  
                            "label":label,
                            "startDate":datefrom,
                            "endDate":dateto, 
                            "outlet" : outlet,
                            "brand": brands, 
                            "supcode":supcode,
                            "bf_amount":input1.replace(',', ''),
                            "rebate_method":[
                            {
                                "range":0,
                                "type":'%',
                                "value":0
                            } 
                            ]
                        }

                        if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                            #to cal gr_sum 
                            result = rims_data_functions.gr_sum(data)    
                            if result['status'] == live_mode:  
                                calval_method = 'non_tier'
                                add_data = create_inv_header_child(data, result, calval_method)  
                            else:
                                    error_log(list_guid, 'check_tta', data, result)
                
            except KeyError:
                # Key is not present
                pass 
        
        #administration_fees 
        for fee_key, fee_value in administration_fees.items():
            # Skip non-fee fields
            if fee_key not in ['list_guid', 'list_link_guid', 'revision', 'created_at', 'created_by', 'updated_at', 'updated_by', 'customer_guid']:
                if fee_value > 0:  # Check if fee is applicable
                    if fee_key.endswith('_value'):  # Check if it's a fee value field
                        fee_type_key = fee_key.replace('_value', '_type')
                        fee_type_value = administration_fees[fee_type_key]
                        q_type = 'Yearly'  # Default type, change as necessary

                        if fee_type_value in ['GPV', 'NPV', 'Monthly', 'Yearly']:
                            q_type = 'gr_gross_sum' if fee_type_value == 'GPV' else 'gr_net_sum' if fee_type_value == 'NPV' else 'Monthly' if fee_type_value == 'Monthly' else 'Yearly'

                        data = {
                            "customer_guid": customer_guid,
                            "refno": result_1.refno,
                            "code": result_1.supplier_code,
                            "name": result_1.supplier_name,
                            "prefix1": fee_type_value,
                            "type": q_type,
                            "label": fee_key.replace('_value', ''),
                            "startDate": datefrom,
                            "endDate": dateto,
                            "outlet": outlet,
                            "brand": brands,
                            "supcode": supcode,
                            "bf_amount": fee_value,
                            "rebate_method": [
                                {
                                    "range": Decimal(0.00),
                                    "type": '%',
                                    "value": Decimal(0.00)
                                }
                            ]
                        }
                        result = rims_data_functions.gr_sum(data)
                        if result['status'] == live_mode:
                            calval_method = 'non_tier'
                            add_data = create_inv_header_child(data, result, calval_method)
                        else:
                            error_log(list_guid, 'check_tta', data, result)

        #business_growth_support
        query_bgs = consolidate_result[0].business_growth_support
        for bgs in query_bgs:
            try:
                if(bgs['calMethod'] == 'Method1'):
                    try:
                        #got date range then how
                        if(bgs['daterange']):
                            bgs_from = datetime.strptime(bgs['daterange']['from'],'%Y-%m-%d')
                            bgs_to = datetime.strptime(bgs['daterange']['to'],'%Y-%m-%d')

                            check_daterange = daterange_condition(bgs['label'], cal_date, bgs['daterange']['from'], bgs['daterange']['to']) 
                            # print(bgs['label'])

                            if(bgs['input1'] > '0.00' ):
                                if bgs['radio1']['value'] == 'GPV':
                                    q_type = 'gr_gross_sum'
                                elif  bgs['radio1']['value'] == 'NPV':
                                    q_type = 'gr_net_sum'
                                elif  bgs['radio1']['value'] == 'Monthly':
                                    q_type = 'Monthly'
                                elif  bgs['radio1']['value'] == 'Yearly':
                                    q_type = 'Yearly'   
                                else:
                                    q_type = 'unknown'

                                field = bgs['field']
                                label = bgs['label']
                                input1 = bgs['input1']
                                radio = bgs['radio1']['value']
                                prefix1 = bgs['prefix1']['value']

                                calmethod = 'sum_method'

                                if calmethod == 'sum_method': 
                                    data = {
                                        "customer_guid":customer_guid, 
                                        "refno":result_1.refno, 
                                        "code":result_1.supplier_code, 
                                        "name":result_1.supplier_name, 
                                        "prefix1": prefix1,
                                        "type":q_type,  
                                        "label":label, 
                                        "startDate":check_daterange['date_from'],
                                        "endDate":check_daterange['date_to'], 
                                        "outlet" : outlet,
                                        "brand": brands,
                                        "supcode":supcode,
                                        "bf_amount":input1.replace(',', ''),
                                        "rebate_method":[
                                        {
                                            "range":0,
                                            "type":'%',
                                            "value":0
                                        } 
                                        ]
                                    }

                                if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                    #to cal gr_sum 
                                    result = rims_data_functions.gr_sum(data)    
                                    if result['status'] == live_mode:  
                                        calval_method = 'non_tier'
                                        add_data = create_inv_header_child(data, result, calval_method)   
                                    else:
                                        error_log(list_guid, 'check_tta', data, result) 
                            
                    except:
                        #no date range method
                        #print('no daterange', bgs['label'])
                        if(bgs['input1'] > '0.00' ):
                            if bgs['radio1']['value'] == 'GPV':
                                q_type = 'gr_gross_sum'
                            elif  bgs['radio1']['value'] == 'NPV':
                                q_type = 'gr_net_sum'
                            elif  bgs['radio1']['value'] == 'Monthly':
                                    q_type = 'Monthly'
                            elif  bgs['radio1']['value'] == 'Yearly':
                                    q_type = 'Yearly'  
                            else:
                                q_type = 'unknown'

                            field = bgs['field']
                            label = bgs['label']
                            input1 = bgs['input1']
                            radio = bgs['radio1']['value']
                            prefix1 = bgs['prefix1']['value']

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": prefix1,
                                    "type":q_type,  
                                    "label":label, 
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":input1.replace(',', ''),
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }
                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                #to cal gr_sum 
                                result = rims_data_functions.gr_sum(data)    
                                if result['status'] == live_mode:  
                                    calval_method = 'non_tier'
                                    add_data = create_inv_header_child(data, result, calval_method)   
                                else:
                                    error_log(list_guid, 'check_tta', data, result) 

            except KeyError:
                pass

        #promotion_support
        query_ps  = consolidate_result[0].promotion_support
        for ps in query_ps:
            try:
                if(ps['calMethod'] == 'Method1'):
                    try: 
                        #got date range then how
                        if(ps['daterange']):  

                            # ps_from = datetime.strptime(ps['daterange']['from'],'%Y-%m-%d')
                            # ps_to = datetime.strptime(ps['daterange']['to'],'%Y-%m-%d')
                            
                            check_daterange = daterange_condition(ps['label'], cal_date, ps['daterange']['from'], ps['daterange']['to'])
                        
                            if(ps['input1'] > '0.00' ):
                                if ps['radio1']['value'] == 'GPV':
                                    q_type = 'gr_gross_sum'
                                elif  ps['radio1']['value'] == 'NPV':
                                    q_type = 'gr_net_sum'
                                elif  ps['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                                elif  ps['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'  
                                else:
                                    q_type = 'unknown'

                                field = ps['field']
                                label = ps['label']
                                input1 = ps['input1']
                                radio = ps['radio1']['value']
                                prefix1 = ps['prefix1']['value']

                                calmethod = 'sum_method'

                                if calmethod == 'sum_method': 
                                    data = {
                                        "customer_guid":customer_guid, 
                                        "refno":result_1.refno, 
                                        "code":result_1.supplier_code, 
                                        "name":result_1.supplier_name, 
                                        "prefix1": prefix1,
                                        "type":q_type,  
                                        "label":label, 
                                        "startDate":check_daterange['date_from'],
                                        "endDate":check_daterange['date_to'], 
                                        "outlet" : outlet,
                                        "brand": brands,
                                        "supcode":supcode,
                                        "bf_amount":input1.replace(',', ''), 
                                        "rebate_method":[
                                        {
                                            "range":0,
                                            "type":'%',
                                            "value":0
                                        } 
                                        ]
                                    }
                                # error_log(list_guid, 'check_tta', data, '')
                                if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                    #to cal gr_sum 
                                    result = rims_data_functions.gr_sum(data)  
                                    if result['status'] == live_mode:  
                                        calval_method = 'non_tier' 
                                        add_data = create_inv_header_child(data, result, calval_method)   
                                    else:
                                        error_log(list_guid, 'check_tta', data, result)  
                                
                    except:
                        #no date range method
                        #print('no daterange', ps['label'])
                        if(ps['input1'] > '0.00' ):
                            if ps['radio1']['value'] == 'GPV':
                                q_type = 'gr_gross_sum'
                            elif  ps['radio1']['value'] == 'NPV':
                                q_type = 'gr_net_sum'
                            elif  ps['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                            elif  ps['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'      
                            else:
                                q_type = 'unknown'

                            field = ps['field']
                            label = ps['label']
                            input1 = ps['input1']
                            radio = ps['radio1']['value']
                            prefix1 = ps['prefix1']['value']

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": prefix1,
                                    "type":q_type,  
                                    "label":label, 
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":input1.replace(',', ''),
                                    
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }
                            # error_log(list_guid, 'check_tta', data, '')
                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                #to cal gr_sum 
                                result = rims_data_functions.gr_sum(data)    
                                if result['status'] == live_mode:  
                                    calval_method = 'non_tier'
                                    add_data = create_inv_header_child(data, result, calval_method)  
                                else:
                                    error_log(list_guid, 'check_tta', data, result) 
            except KeyError:
                pass

        #marketing_support
        query_ms  = consolidate_result[0].marketing_support
        for ms in query_ms:
            try:
                if(ms['calMethod'] == 'Method1'):
                    try:
                        #got date range then how
                        if(ms['daterange']):
                            ms_from = datetime.strptime(ms['daterange']['from'],'%Y-%m-%d')
                            ms_to = datetime.strptime(ms['daterange']['to'],'%Y-%m-%d')

                            check_daterange = daterange_condition(ms['label'], cal_date, ms['daterange']['from'], ms['daterange']['to'])

                            # if ms_from <= cal_date <= ms_to:
                            #     datefrom1 = cal_date.replace(day=1).strftime('%Y-%m-%d')
                            #     dateto1 = str(last_day_of_month(datetime.date(cal_date)))
                            # elif ms_to <= cal_date : 
                            #     datefrom1 =  str(ms_to).strftime('%Y-%m-%d')
                            #     dateto1 = str(ms_to).strftime('%Y-%m-%d')
                            # else:
                            #     datefrom1 = '2099-12-01'
                            #     dateto1 =  '2099-12-31'  
                            # print(bgs['label'])

                            if(ms['input1'] > '0.00' ):
                                if ms['radio1']['value'] == 'GPV':
                                    q_type = 'gr_gross_sum'
                                elif  ms['radio1']['value'] == 'NPV':
                                    q_type = 'gr_net_sum'
                                elif  ms['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                                elif  ms['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'  
                                else:
                                    q_type = 'unknown'

                                field = ms['field']
                                label = ms['label']
                                input1 = ms['input1']
                                radio = ms['radio1']['value']
                                prefix1 = ms['prefix1']['value']

                                calmethod = 'sum_method'

                                if calmethod == 'sum_method': 
                                    data = {
                                        "customer_guid":customer_guid, 
                                        "refno":result_1.refno, 
                                        "code":result_1.supplier_code, 
                                        "name":result_1.supplier_name, 
                                        "prefix1": prefix1,
                                        "type":q_type,  
                                        "label":label, 
                                        "startDate":check_daterange['date_from'],
                                        "endDate":check_daterange['date_to'], 
                                        "outlet" : outlet,
                                        "brand": brands,
                                        "supcode":supcode,
                                        "bf_amount":input1.replace(',', ''),
                                        "rebate_method":[
                                        {
                                            "range":0,
                                            "type":'%',
                                            "value":0
                                        } 
                                        ]
                                    }

                                if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                    #to cal gr_sum 
                                    result = rims_data_functions.gr_sum(data)    
                                    if result['status'] == live_mode:  
                                        calval_method = 'non_tier'
                                        add_data = create_inv_header_child(data, result, calval_method)   
                                    else:
                                        error_log(list_guid, 'check_tta', data, result)  

                            
                    except:
                        #no date range method
                        #print('no daterange', ms['label'])
                        if(ms['input1'] > '0.00' ):
                            if ms['radio1']['value'] == 'GPV':
                                q_type = 'gr_gross_sum'
                            elif  ms['radio1']['value'] == 'NPV':
                                q_type = 'gr_net_sum'
                            elif  ms['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                            elif  ms['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'  
                            else:
                                q_type = 'unknown'

                            field = ms['field']
                            label = ms['label']
                            input1 = ms['input1']
                            radio = ms['radio1']['value']
                            prefix1 = ms['prefix1']['value']

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": prefix1,
                                    "type":q_type,  
                                    "label":label, 
                                    "startDate":datefrom,
                                    "endDate":dateto,  
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":input1.replace(',', ''),
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                #to cal gr_sum 
                                result = rims_data_functions.gr_sum(data)    
                                if result['status'] == live_mode:  
                                    calval_method = 'non_tier'
                                    add_data = create_inv_header_child(data, result, calval_method)  
                                else:
                                    error_log(list_guid, 'check_tta', data, result) 

            except KeyError:
                pass

        #e_commerce_support
        query_ecs  = consolidate_result[0].e_commerce_support
        for ecs in query_ecs:
            try:
                if(ecs['calMethod'] == 'Method1'):
                    try:
                        #got date range then how
                        if(ecs['daterange']): 
                            ecs_from = datetime.strptime(ecs['daterange']['from'],'%Y-%m-%d')
                            ecs_to = datetime.strptime(ecs['daterange']['to'],'%Y-%m-%d')

                            check_daterange = daterange_condition(ecs['label'], cal_date, ecs['daterange']['from'], ecs['daterange']['to'])

                            if(ecs['input1'] > '0.00' ):
                                if ecs['radio1']['value'] == 'GPV':
                                    q_type = 'gr_gross_sum'
                                elif  ecs['radio1']['value'] == 'NPV':
                                    q_type = 'gr_net_sum'
                                elif  ecs['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                                elif  ecs['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'  
                                else:
                                    q_type = 'unknown'

                                field = ecs['field']
                                label = ecs['label']
                                input1 = ecs['input1']
                                radio = ecs['radio1']['value']
                                prefix1 = ecs['prefix1']['value']

                                calmethod = 'sum_method'

                                if calmethod == 'sum_method': 
                                    data = {
                                        "customer_guid":customer_guid, 
                                        "refno":result_1.refno, 
                                        "code":result_1.supplier_code, 
                                        "name":result_1.supplier_name, 
                                        "prefix1": prefix1,
                                        "type":q_type,  
                                        "label":label, 
                                        "startDate":check_daterange['date_from'],
                                        "endDate":check_daterange['date_to'], 
                                        "outlet" : outlet,
                                        "brand": brands,
                                        "supcode":supcode,
                                        "bf_amount":input1.replace(',', ''),
                                        "rebate_method":[
                                        {
                                            "range":0,
                                            "type":'%',
                                            "value":0
                                        } 
                                        ]
                                    }

                                if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                    #to cal gr_sum 
                                    result = rims_data_functions.gr_sum(data)    
                                    if result['status'] == live_mode:  
                                        calval_method = 'non_tier'
                                        add_data = create_inv_header_child(data, result, calval_method)   
                                    else:
                                        error_log(list_guid, 'check_tta', data, result)  


                            
                    except:
                        #no date range method
                        #print('no daterange', ecs['label'])
                        if(ecs['input1'] > '0.00' ):
                            if ecs['radio1']['value'] == 'GPV':
                                q_type = 'gr_gross_sum'
                            elif  ecs['radio1']['value'] == 'NPV':
                                q_type = 'gr_net_sum'
                            elif  ecs['radio1']['value'] == 'Monthly':
                                        q_type = 'Monthly'
                            elif  ecs['radio1']['value'] == 'Yearly':
                                        q_type = 'Yearly'  
                            else:
                                q_type = 'unknown'

                            field = ecs['field']
                            label = ecs['label']
                            input1 = ecs['input1']
                            radio = ecs['radio1']['value']
                            prefix1 = ecs['prefix1']['value']

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": prefix1,
                                    "type":q_type,  
                                    "label":label, 
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":input1.replace(',', ''),
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'): 
                                #to cal gr_sum 
                                result = rims_data_functions.gr_sum(data)    
                                if result['status'] == live_mode:  
                                    calval_method = 'non_tier'
                                    add_data = create_inv_header_child(data, result, calval_method)  
                                else:
                                    error_log(list_guid, 'check_tta', data, result) 
            except KeyError:
                pass

        result_status = result['status']

        data = {
            "status": result_status,
            "message": list_guid_array,
            "retailer_guid": customer_guid
        }
                            
      
        #return data
        #print(result['status'])
        if result_status == False:
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(data, status=status.HTTP_200_OK)
        #return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

        #return Response({"status":"true","result":list_guid_array})   
    else:
        return HttpResponse("Invalid Method")


# Create your views here.
