# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import serializers
# #from django.core import serializers
# import requests
# import json
# from _lib import panda
# from django.db import connection
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status,viewsets
# from collections import defaultdict
# from django.http import QueryDict
# from rest_framework.permissions import IsAuthenticated

# from _ts_tta_invmain.serializers import TtaInvmainSerializer 
# from _ts_tta_invmain.models import TtaInvmain
# from _ts_tta_invchild.serializers import TtaInvchildSerializer 
# from _ts_tta_invchild.models import TtaInvchild

# from .serializers import update_ttachild_serializers

from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.core import serializers
import requests
import json
import uuid
import calendar
import cProfile
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

from io import StringIO
from io import BytesIO
import xlsxwriter
import pandas as pd
import numpy
#from django.http import HttpResponse

from _mc_tta_list_cal_main.models import TtaListCalMain 
from _mc_tta_list.models import TtaList
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from _ml_rims_brand.models import RimsBrand
from _ml_rims_supcus.models import RimsSupcus
from _ts_tta_cal_log.models import TtaListCalLogs
from _ts_tta_cal_log.serializers import TtaListCalLogsSerializer 
from _ts_tta_invmain.models import TtaInvmain
from _ts_tta_invmain.serializers import TtaInvmainSerializer 
from _ts_tta_invchild.models import TtaInvchild
from _ts_tta_invchild.serializers import TtaInvchildSerializer

from .serializers import update_ttachild_serializers
from _mc_get_customer_profile.models import CustomerProfile

import ctypes  # An included library with Python install.   
import threading

# Create your serializers here.

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def invchild_insert(request,invmain_guid):
    if request.method == 'POST': 
        #method 1
        # serializer = TtaInvchildSerializer(data=json.loads(request.data['inv_child']), many=True) 
        # if serializer.is_valid():
        #     print(serializer.data) 
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #method 2
        # json_child = json.loads(request.data['inv_child'])

        # for input_child in json_child:
        #     if 'invchild_guid' in input_child:
        #         #update 
        #         entry = TtaInvchild.objects.get(pk=input_child['invchild_guid']) 
        #         del input_child['invmain_guid']

        #         for key, value in input_child.items(): 
        #             entry.update_field(key, value)
        #         entry.save(update_fields=input_child.keys()) # This will only save the updated keys
        #     else:
                
        #         #insert
        #         aa = []
        #         aa.append(input_child)
        #         print(aa)
        #         serializer = TtaInvchildSerializer(data=aa , many=True) 
        #         if serializer.is_valid():
        #             serializer.save()
        #         else:
        #             print(serializer.errors)
        #             return Response('sad')
                
        
        # return Response('ok')

        #method 3
        json_child = json.loads(request.data['inv_child'])

        print(json_child)

        for input_child in json_child:
            if 'invchild_guid' in input_child:   
                serializer = update_ttachild_serializers(data=input_child) 
                if serializer.is_valid() != False:  
                    obj = TtaInvchild.objects.get(pk=input_child['invchild_guid'])   
                    for k in input_child:
                        if k != 'invmain_guid': 
                            setattr(obj, k , input_child[k])
                    obj.save()
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                print('insert')  
                serializer = TtaInvchildSerializer(data=input_child)  
                if serializer.is_valid() != False:  
                    serializer.save() 
                else:
                    print(serializer.errors)
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
        return Response('SUCCESS', status=status.HTTP_201_CREATED)

    # return Response('Done')     

@api_view(['POST'])
def invchild_delete(request,invmain_guid):
    if request.method == 'POST':  
        #method 3
        json_child = json.loads(request.data['inv_child'])

        #print(json_child)
        for input_child in json_child:
            if 'invchild_guid' in input_child:
                instance = TtaInvchild.objects.get(invchild_guid=input_child['invchild_guid'])
                instance.delete() 
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


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
    print(f"Data type: {type(data)}")
    print(f"Data content: {data}")
    print(f"Result type: {type(result)}")
    print(f"Result content: {result}")

    if calval_method == 'non_tier':
        if result['value'] != 0:
            if data['prefix1'] == '%': 
                cal_val = round((float(data['bf_amount']) * float(result['value'])) / 100, 2)
            else:
                cal_val = data['bf_amount']
        else:
            cal_val = 0      
    elif calval_method == 'tier':   
        cal_val = 1
    else:
        cal_val = result['value'] 

    try: 
        check_invmain_exist = TtaInvmain.objects.get(docno=data['refno'], customer_guid=data['customer_guid']) 
    except TtaInvmain.DoesNotExist:
        try:
            customer_profile = CustomerProfile.objects.get(customer_guid=data['customer_guid'])
        except CustomerProfile.DoesNotExist:
            print("CustomerProfile with the given customer_guid does not exist.")
            return

        check_invmain_exist = TtaInvmain(
            docno=data['refno'],
            customer_guid=customer_profile,
            invoice_date=date.today(),
            code=data['code'],
            name=data['name'],
            created_by='system',
            updated_by='system'
        )
        check_invmain_exist.save()   

        update_profile = TtaList.objects.filter(refno=data['refno'], customer_guid=data['customer_guid']).values(
            'bill_supp_name', 'supplier_add1', 'supplier_add2', 'supplier_add3', 'supplier_add4', 'supplier_pic'
        )

        if update_profile.exists():
            profile = update_profile[0]
            add1 = profile['supplier_add1']
            add2 = profile['supplier_add2']
            add3 = profile['supplier_add3']
            add4 = profile['supplier_add4']
            pic = profile['supplier_pic']
            
            TtaInvmain.objects.filter(docno=data['refno'], customer_guid=data['customer_guid']).update(
                add_1=add1,
                add_2=add2,
                add_3=add3,
                add_4=add4,
                attn=pic
            )
                                    
    get_invmainguid = TtaInvmain.objects.get(docno=data['refno'], customer_guid=data['customer_guid']) 

    if cal_val != 0:   
        if calval_method == 'tier':
            for t_loop in result['rebate']: 
                t = 1
                if t_loop['rebateValue'] != 0: 
                    try:
                        check_invchild_exist = TtaInvchild.objects.get(
                            invmain_guid=get_invmainguid,
                            customer_guid=data['customer_guid'],
                            description=data['label'] + str(t)
                        )
                        check_invchild_exist.totalprice = t_loop['rebateValue']
                        check_invchild_exist.total_incl_tax = t_loop['rebateValue']
                        check_invchild_exist.updated_by = 'system'
                        check_invchild_exist.save()
                    except TtaInvchild.DoesNotExist:
                        query_line = TtaInvchild.objects.filter(invmain_guid=get_invmainguid, customer_guid=data['customer_guid'])
                        line = query_line.count() + 1  
                        check_invchild_exist = TtaInvchild(
                            customer_guid=data['customer_guid'],
                            invmain_guid=get_invmainguid,
                            line=line,
                            description=data['label'] + str(t),
                            pricetype=data['prefix1'],
                            unit_price=data['bf_amount'],
                            qty='1', 
                            totalprice=t_loop['rebateValue'],
                            total_incl_tax=t_loop['rebateValue'],
                            created_by='system',
                            updated_by='system'
                        ) 
                        check_invchild_exist.save()
                    t = t + 1 
        else:
            try:
                check_invchild_exist = TtaInvchild.objects.get(
                    invmain_guid=get_invmainguid,
                    customer_guid=customer_guid,
                    description=data['label']
                )
                check_invchild_exist.totalprice = cal_val
                check_invchild_exist.total_incl_tax = cal_val
                check_invchild_exist.updated_by = 'system'
                check_invchild_exist.save()
            except TtaInvchild.DoesNotExist:
                query_line = TtaInvchild.objects.filter(invmain_guid=get_invmainguid, customer_guid=customer_guid)
                line = query_line.count() + 1  
                check_invchild_exist = TtaInvchild(
                    customer_guid=customer_guid,
                    invmain_guid=get_invmainguid,
                    line=line,
                    description=data['label'],
                    pricetype=data['prefix1'],
                    unit_price=data['bf_amount'],
                    qty='1',
                    totalprice=cal_val,
                    total_incl_tax=cal_val,
                    created_by='system',
                    updated_by='system'
                ) 
                check_invchild_exist.save()

    print("Check InvMain: ", check_invmain_exist)
    return result


def error_log(list_guid, log_module, data, result):
        
        log = TtaListCalLogs(
                    log_guid=panda.panda_uuid()
                    , customer_guid=data['customer_guid']
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
        list_guid_array = request_data['list_guid']
        consolidate_result = []

        print("Request Data: ", request_data)

        #loop through  list_guid that need to undergo data processing
        for list_guid in list_guid_array:   
            result_1 = TtaList.objects.get(customer_guid=customer_guid, list_guid=list_guid)  
            consolidate_result.append(result_1)   
        
        force_new_dict = {}

        final_list =[]

        for result_1 in consolidate_result:
            force_new_dict['list_guid'] = result_1.list_guid
            val_supplier_guid = result_1.supplier_guid
            supplier_name = result_1.supplier_name
            # Process 'supplier_name' field
            if supplier_name:
                if type(val_supplier_guid) == str: 
                    val_supplier_guid = list(val_supplier_guid.split(" "))  
                q_supcode = RimsSupcus.objects.filter(supcus_guid__in=val_supplier_guid).filter(customer_guid=customer_guid).values_list('code', flat=True)
                supcode = list(q_supcode) 
                force_new_dict['supcode'] = supcode
                force_new_dict['sup_guid'] = val_supplier_guid
                tobecopy = force_new_dict

                final = tobecopy.copy()
                final_list.append(final)  
                print("Final List: ", final_list)
    
        return Response({"status":"true","result":final_list}) 
        #return Response({"status":"true","result":outlet})   

        '''
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
    '''
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

        # Initialize result at the beginning
        result = None
        
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
        for result_1 in consolidate_result:
            supplier_guid = result_1.supplier_guid
            supplier_name = result_1.supplier_name
            outlet_type = result_1.outlet_type

        #Numbers of List
        outlet_list = []
        exclude_outlet_list = []
        trading_brand_list = []
        purchase_list = []
        payment_list = []
        stock_list = []
        administration_list = []
        business_growth_support_list = []
        promotion_support_list = []
        marketing_support_list = []
        e_commerce_support_list = []
          
        for list_guid in list_guid_array:
            result_1 = TtaList.objects.get(customer_guid=customer_guid, list_guid=list_guid)
            outlet_list.append(result_1.outlet.values()) 
            exclude_outlet_list.append(result_1.exclude_outlet.values_list('tta_exclude_outlet_guid', flat=True))
            trading_brand_list.extend(result_1.trading_brand.values_list('brand_guid_id', flat=True)) 
            purchase_list.append(result_1.purchase_n_rebates)
            payment_list.append(result_1.payment_n_discount)
            stock_list.append(result_1.stock_n_deliveries)
            administration_list.append(result_1.administration_fees)
            business_growth_support_list.append(result_1.business_growth_support)
            promotion_support_list.append(result_1.promotion_support)
            marketing_support_list.append(result_1.marketing_support)
            e_commerce_support_list.append(result_1.e_commerce_support)

        #Outlet
        print("Outlet Type: ", outlet_type)

        outlet_branch_guids = []

        for outlet_item in outlet_list:
            for item in outlet_item:
                #print("Outlet Item: ", item)
                outlet_branch_guids.append(item['branch_guid_id'])  # Accessing the 'branch_guid' key of the dictionary

        # Process each field individually using the extracted values
        if outlet_type == "All":
            q_outlet = RimsCpSetBranch.objects.exclude(set_active=0).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        elif outlet_type == "Outlet":
            q_outlet = RimsCpSetBranch.objects.filter(branch_guid__in=outlet_branch_guids).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        else:
            outlet = []  # Default value when conditions don't match

        
        print("Outlet Info: ", outlet)

        #Exclude Outlet
        print("Exclude Outlet List: ", exclude_outlet_list)

        tta_exclude_outlet_guids = []

        for exclude_item in exclude_outlet_list:
            print("Brand Item: ", exclude_item)
            tta_exclude_outlet_guids.append(exclude_item) 
        
        # Process each field individually using the extracted values
        if len(exclude_outlet_list) != 0:  # Fixing the if condition
            q_brand = RimsCpSetBranch.objects.exclude(set_active=0).exclude(branch_guid__in=tta_exclude_outlet_guids).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        else:
            outlet = []  # Default value when conditions don't match

        print("Exclude Outlet Info: ", outlet)

        #Trading Brand
        print("Trading Brand List: ", trading_brand_list)

        trading_brand_guids = []

        for brand_item in trading_brand_list:
            print("Brand Item: ", brand_item)
            trading_brand_guids.append(brand_item) 

        # Process each field individually using the extracted values
        if len(trading_brand_list) != 0:  # Fixing the if condition
            q_brand = RimsBrand.objects.filter(brand_guid__in=trading_brand_guids, customer_guid=customer_guid).values_list('code', flat=True)
            brands = list(q_brand)
        else:
            brands = []  # Default value when conditions don't match

        print("Trading Brand Info: ", brands)

        # Process 'supplier_name' field
        if supplier_name:
            val_supplier_guid = supplier_guid.split()
            q_supcode = RimsSupcus.objects.filter(supcus_guid__in=val_supplier_guid).filter(customer_guid=customer_guid).values_list('code', flat=True)
            supcode = list(q_supcode)

        #Purchase N Rebates
        print("Purchase List: ", purchase_list)
            
        # Define the rebate fields to look for
        rebate_fields = [
            "unconditional_rebate_value", "commission_value", "auto_replenishment_rebate_value",
            "common_assortment_rebate_value", "monthly_discount_value",
            "target_purchase_tier_1_value1", "target_purchase_tier_1_value2", "target_purchase_tier_2_value1",
            "target_purchase_tier_2_value2", "target_purchase_tier_3_value1", "target_purchase_tier_3_value2",
            "target_growth_tier_1_value1", "target_growth_tier_1_value2", "target_growth_tier_2_value1",
            "target_growth_tier_2_value2", "target_growth_tier_3_value1", "target_growth_tier_3_value2"
        ]

        for purchase in purchase_list:
            print("Processing Purchase and Rebates: ", purchase.refno)

            tier_results = []

            for rebate_key in rebate_fields:
                rebate_value = getattr(purchase, rebate_key, None)
                if rebate_value is not None and rebate_value > 0.0:
                    print(f"Key: {rebate_key}, Value: {rebate_value}")

                    # Determine the appropriate fee_type_key and fee_value_type_key
                    if '_value1' in rebate_key:
                        rebate_type_key = rebate_key.replace('_value1', '_type1')
                        rebate_value_type_key = rebate_key.replace('_value1', '_value_type')
                    elif '_value2' in rebate_key:
                        rebate_type_key = rebate_key.replace('_value2', '_type2')
                        rebate_value_type_key = rebate_key.replace('_value2', '_value_type')
                    else:
                        rebate_type_key = rebate_key.replace('_value', '_type')
                        rebate_value_type_key = rebate_key.replace('_value', '_value_type')

                    rebate_type_value = getattr(purchase, rebate_type_key, None)
                    rebate_value_type_value = getattr(purchase, rebate_value_type_key, None)

                    if rebate_type_value is not None and rebate_value_type_value is not None:
                        print("Rebate Value: ", rebate_value)
                        print("Rebate Type Key: ", rebate_type_key)
                        print("Rebate Type Value: ", rebate_type_value)
                        print("Rebate Value Type Key: ", rebate_value_type_key)
                        print("Rebate Value Type Value: ", rebate_value_type_value)

                        q_type = 'gr_gross_sum' if rebate_value_type_value == 'GPV' else 'gr_net_sum' if rebate_value_type_value == 'NPV' else 'Monthly' if rebate_value_type_value == 'Monthly' else 'Yearly' if rebate_value_type_value == 'Yearly' else 'unknown'
                        
                        # Handle labels properly
                        label = rebate_key.replace('_value1', '_Value 1').replace('_value2', '_Value 2').replace('_value', '').replace('_', ' ').title()

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

                        print("Data Prepared: ", data)

                        if q_type in ['gr_gross_sum', 'gr_net_sum']:
                            # To calculate gr_sum
                            result = rims_data_functions.gr_sum(data)
                            print("Result: ", result)

                            if result['status'] == live_mode:
                                calval_method = 'non_tier'
                                print("Calling create_inv_header_child with calval_method:", calval_method)
                                print("Data:", data)
                                print("Result:", result)
                                add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                print("Function executed successfully with result:", add_data)
                            else:
                                error_log(list_guid, 'check_tta', data, result)
                        else:
                            # If it's a tiered rebate, collect tier results
                            if 'target_purchase_tier' in rebate_key or 'target_growth_tier' in rebate_key:
                                tier_result = {
                                    "range": Decimal(rebate_value),
                                    "type": rebate_value_type_value,
                                    "value": Decimal(rebate_type_value)
                                }
                                tier_results.append(tier_result)
                    else:
                        print(f"Skipping {rebate_key}: Missing type values")
                else:
                    print(f"Skipping {rebate_key}: Value is None or zero")

            # Handle tiered results if any
            if len(tier_results) > 0:
                # Get the last day of the month from a given date  
                dt = datetime.strptime(dateto, '%Y-%m-%d') 
                input_dt = datetime(dt.year, dt.month, dt.day)  
                month, year = (input_dt.month-1, input_dt.year) if input_dt.month != 1 else (12, input_dt.year-1) 
                aa_last_month = input_dt.replace(day=1, month=month, year=year)
                actual_last_day_of_month = last_day_of_month(aa_last_month).strftime('%Y-%m-%d')

                bf_data = {
                    "customer_guid": customer_guid,
                    "refno": result_1.refno,
                    "code": result_1.supplier_code,
                    "name": result_1.supplier_name,
                    "prefix1": tier_results[0]['type'],
                    "type": q_type,
                    "label": label,
                    "startDate": consolidate_result[0].tta_period_from,
                    "endDate": actual_last_day_of_month,
                    "outlet": outlet,
                    "brand": brands,
                    "supcode": supcode,
                    "bf_amount": Decimal(0.00),
                    "rebate_method": [
                        {
                            "range": Decimal(0.00),
                            "type": '%',
                            "value": Decimal(0.00)
                        }
                    ]
                }

                bf_result = rims_data_functions.gr_sum(bf_data)
                final_bf_result = bf_result['value']
                print("Tier Calculation bf_result:", bf_result)

                data = {
                    "customer_guid": customer_guid,
                    "refno": result_1.refno,
                    "code": result_1.supplier_code,
                    "name": result_1.supplier_name,
                    "prefix1": tier_results[0]['type'],
                    "label": label,
                    "type": q_type,
                    "startDate": datefrom,
                    "endDate": dateto,
                    "outlet": outlet,
                    "brand": brands,
                    "supcode": supcode,
                    "bf_amount": final_bf_result,
                    "rebate_method": tier_results
                }

                print("Tier Data Prepared:", data)

                result = rims_data_functions.rebate(data)
                print("Tier Result:", result)

                if result['status'] == live_mode:
                    calval_method = 'tier'
                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                    print("Function executed successfully with result:", add_data)
                else:
                    error_log(list_guid, 'check_tta', data, result)

        # Debugging the complete dictionary to see all keys and values
        for purchase in purchase_list:
            print("Debugging complete purchase object:", vars(purchase))

        #Payment N Discount
        print("Payment List: ", payment_list)

        # Define the discount fields to look for
        discount_fields = [
            "early_payment_terms_value", "early_payment_discount_value", "prompt_payment_discount_value"
        ]

         # Iterating over each payment and discount object
        for payment in payment_list:
            print("Processing Payment and Discount: ", payment.refno)

            for discount_key in discount_fields:
                discount_value = getattr(payment, discount_key, None)
                if discount_value is not None and discount_value > 0.0:
                    print(f"Key: {discount_key}, Value: {discount_value}") 

                 # Determine the appropriate fee_type_key and fee_value_type_key
                    if '_value1' in discount_key:
                        discount_type_key = discount_key.replace('_value1', '_type1') 
                        discount_value_type_key = discount_key.replace('_value1', '_value_type')
                    elif '_value2' in discount_key:
                        discount_type_key = discount_key.replace('_value2', '_type2')
                        discount_value_type_key = discount_key.replace('_value2', '_value_type')
                    else:
                        discount_type_key = discount_key.replace('_value', '_type')
                        discount_value_type_key = discount_key.replace('_value', '_value_type')

                    discount_type_value = getattr(payment, discount_type_key, None)
                    discount_value_type_value = getattr(payment, discount_value_type_key, None)

                    if discount_type_value is not None and discount_value_type_value is not None:
                        print("Discount Value: ", discount_value)
                        print("Discount Type Key: ", discount_type_key)
                        print("Discount Type Value: ", discount_type_value)
                        print("Discount Value Type Key: ", discount_value_type_key)
                        print("Discount Value Type Value: ", discount_value_type_value)
                    
                        q_type = 'gr_gross_sum' if discount_value_type_value == 'GIV' else 'gr_net_sum' if discount_value_type_value == 'NPV' else 'Monthly' if discount_value_type_value == 'Monthly' else 'Yearly' if discount_value_type_value == 'Yearly' else 'unknown'

                        label = discount_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)

                        data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": discount_type_value,
                                    "label":label,
                                    "type":q_type,  
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":discount_value,
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }

                        print("Data Prepared: ", data)

                        if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                            # To calculate gr_sum
                            result = rims_data_functions.gr_sum(data)
                            print("Result: ", result)
                            
                            if result['status'] == live_mode:
                                calval_method = 'non_tier'
                                print("Calling create_inv_header_child with calval_method:", calval_method)
                                print("Data:", data)
                                print("Result:", result)
                                
                                add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                print("Function executed successfully with result:", add_data)
                            else:
                                error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {discount_key}: Missing type values")
                
                else:
                    print(f"Skipping {discount_key}: Value is None or zero")

        # Debugging the complete dictionary to see all keys and values
        for payment in payment_list:
            print("Debugging complete payment object:", vars(payment))

        #Stock N Deliveries
        print("Stock List: ", stock_list)

        # Define the stock fields to look for
        stock_fields = [
            "cross_docking_allowance_value", "conventional_flow_thru_allowance_value", "shrinkage_pilferage_allowance_value",
            "non_returnable_goods_allowance_value", "east_malaysia_orders_allowance_value", "damage_good_allowance_value",
            "non_compliance_packaging_allowance_value", "purchase_order_fulfillment_value", "unfulfilled_penalty_value",
            "lost_of_profit_penalty_value", "purchase_order_lead_time_value", "lead_time_penalty_value",
            "ullarge_value", "target_service_level_value", "target_service_level_unfulfilled_penalty_value"
        ]

         # Iterating over each stock and deliveries object
        for stock in stock_list:
            print("Processing Stock and Deliveries: ", stock.refno)

            for stock_key in stock_fields:
                stock_value = getattr(stock, stock_key, None)
                if stock_value is not None and stock_value > 0.0:
                    print(f"Key: {stock_key}, Value: {stock_value}")

                    stock_type_key = stock_key.replace('_value', '_type')
                    stock_type_value = getattr(stock, stock_type_key, None)

                    stock_value_type_key = stock_key.replace('_value', '_value_type')
                    stock_value_type_value = getattr(stock, stock_value_type_key, None)

                    if stock_type_value is not None and stock_value_type_value is not None:
                        print("Stock Value: ", stock_value)
                        print("Stock Type Key: ", stock_type_key)
                        print("Stock Type Value: ", stock_type_value)
                        print("Stock Value Type Key: ", stock_value_type_key)
                        print("Stock Value Type Value: ", stock_value_type_value)

                        q_type = 'gr_gross_sum' if stock_value_type_value == 'GPV' else 'gr_net_sum' if stock_value_type_value == 'NPV' else 'Monthly' if stock_value_type_value == 'Monthly' else 'Yearly' if stock_value_type_value == 'Yearly' else 'unknown'

                        label = stock_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)
                        
                        data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": stock_type_value,
                                    "label":label,
                                    "type":q_type,  
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":stock_value,
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }

                        print("Data Prepared: ", data)

                        if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                            # To calculate gr_sum
                            result = rims_data_functions.gr_sum(data)
                            print("Result: ", result)
                            
                            if result['status'] == live_mode:
                                calval_method = 'non_tier'
                                print("Calling create_inv_header_child with calval_method:", calval_method)
                                print("Data:", data)
                                print("Result:", result)
                                
                                add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                print("Function executed successfully with result:", add_data)
                            else:
                                error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {stock_key}: Missing type values")
                
                else:
                    print(f"Skipping {stock_key}: Value is None or zero")
        
        #Administration Fees
        print("Administration List: ", administration_list)

        # Define the fee fields to look for
        administration_fields = [
            "account_administration_fee_value", "product_registration_fee_value", "sku_replacement_value",
            "new_line_fee_value", "new_item_listing_value", "new_item_first_order_discount_value1",
            "new_item_first_order_discount_value2", "change_of_purchase_type_value", "maintenance_of_vendor_information_value",
            "new_vcr_barcode_value"
        ]

         # Iterating over each administration fees object
        for fee in administration_list:
            print("Processing Administration Fees: ", fee.refno)

            for fee_key in administration_fields:
                fee_value = getattr(fee, fee_key, None)
                if fee_value is not None and fee_value > 0.0:
                    print(f"Key: {fee_key}, Value: {fee_value}")

                # Determine the appropriate fee_type_key and fee_value_type_key
                    if '_value1' in fee_key:
                        fee_type_key = fee_key.replace('_value1', '_type1')
                        fee_value_type_key = fee_key.replace('_value1', '_value_type')
                    elif '_value2' in fee_key:
                        fee_type_key = fee_key.replace('_value2', '_type2')
                        fee_value_type_key = fee_key.replace('_value2', '_value_type')
                    else:
                        fee_type_key = fee_key.replace('_value', '_type')
                        fee_value_type_key = fee_key.replace('_value', '_value_type')

                    fee_type_value = getattr(fee, fee_type_key, None)
                    fee_value_type_value = getattr(fee, fee_value_type_key, None)

                    if fee_type_value is not None and fee_value_type_value is not None:
                        print("Fee Value: ", fee_value)
                        print("Fee Type Key: ", fee_type_key)
                        print("Fee Type Value: ", fee_type_value)
                        print("Fee Value Type Key: ", fee_value_type_key)
                        print("Fee Value Type Value: ", fee_value_type_value)

                        q_type = 'gr_gross_sum' if fee_value_type_value == 'GPV' else 'gr_net_sum' if fee_value_type_value == 'NPV' else 'Monthly' if fee_value_type_value == 'Monthly' else 'Yearly' if fee_value_type_value == 'Yearly' else 'unknown'

                        label = fee_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)
                        
                        data = {
                                    "customer_guid":customer_guid, 
                                    "refno":result_1.refno, 
                                    "code":result_1.supplier_code, 
                                    "name":result_1.supplier_name, 
                                    "prefix1": fee_type_value,
                                    "label":label,
                                    "type":q_type,  
                                    "startDate":datefrom,
                                    "endDate":dateto, 
                                    "outlet" : outlet,
                                    "brand": brands,
                                    "supcode":supcode,
                                    "bf_amount":fee_value,
                                    "rebate_method":[
                                    {
                                        "range":0,
                                        "type":'%',
                                        "value":0
                                    } 
                                    ]
                                }

                        print("Data Prepared: ", data)

                        if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                            # To calculate gr_sum
                            result = rims_data_functions.gr_sum(data)
                            print("Result: ", result)
                            
                            if result['status'] == live_mode:
                                calval_method = 'non_tier'
                                print("Calling create_inv_header_child with calval_method:", calval_method)
                                print("Data:", data)
                                print("Result:", result)
                                
                                add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                print("Function executed successfully with result:", add_data)
                            else:
                                error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {fee_key}: Missing type values")
                
                else:
                    print(f"Skipping {fee_key}: Value is None or zero")
        
        #Business Growth Support
        print("Business Growth Support List: ", business_growth_support_list)

        # Define the bgs fields to look for
        bgs_fields = [
            "category_development_fund_value", "business_development_fund_value", "data_sharing_fee_value",
            "new_store_opening_value", "new_store_first_order_discount_value1", "new_store_first_order_discount_value2",
            "refurbish_store_value", "anniversary_sales_allowance_value", "anniversary_orders_rebate_value"
        ]

        # Iterating over each bgs object
        for bgs in business_growth_support_list:
            print("Processing Business Growth Support: ", bgs.refno)

            for bgs_key in bgs_fields:
                bgs_value = getattr(bgs, bgs_key, None)
                if bgs_value is not None and bgs_value > 0.0:
                    print(f"Key: {bgs_key}, Value: {bgs_value}")

                # Determine the appropriate bgs_type_key and bgs_value_type_key
                    if '_value1' in bgs_key:
                        bgs_type_key = bgs_key.replace('_value1', '_type1')
                        bgs_value_type_key = bgs_key.replace('_value1', '_value_type')
                    elif '_value2' in bgs_key:
                        bgs_type_key = bgs_key.replace('_value2', '_type2')
                        bgs_value_type_key = bgs_key.replace('_value2', '_value_type')
                    else:
                        bgs_type_key = bgs_key.replace('_value', '_type')
                        bgs_value_type_key = bgs_key.replace('_value', '_value_type')

                    bgs_type_value = getattr(bgs, bgs_type_key, None)
                    bgs_value_type_value = getattr(bgs, bgs_value_type_key, None)

                    if bgs_type_value is not None and bgs_value_type_value is not None:
                        print("bgs Value: ", bgs_value)
                        print("bgs Type Key: ", bgs_type_key)
                        print("bgs Type Value: ", bgs_type_value)
                        print("bgs Value Type Key: ", bgs_value_type_key)
                        print("bgs Value Type Value: ", bgs_value_type_value)

                        q_type = 'gr_gross_sum' if bgs_value_type_value == 'GPV' else 'gr_net_sum' if bgs_value_type_value == 'NPV' else 'Monthly' if bgs_value_type_value == 'Monthly' else 'Yearly' if bgs_value_type_value == 'Yearly' else 'unknown'

                        label = bgs_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)

                        # Date range fields
                        date_from_key = bgs_key.replace('_value', '_date_from')
                        date_to_key = bgs_key.replace('_value', '_date_to')
                        date_from = getattr(bgs, date_from_key, None)
                        date_to = getattr(bgs, date_to_key, None)

                        if date_from and date_to:
                            print(f"There is date range for {bgs_key}")

                            bgs_from = datetime.strptime(date_from, '%Y-%m-%d')
                            bgs_to = datetime.strptime(date_to, '%Y-%m-%d')

                            check_daterange = daterange_condition(label, cal_date, date_from, date_to)

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": bgs_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":check_daterange['date_from'],
                                            "endDate":check_daterange['date_to'], 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":bgs_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)
                        else:
                            print(f"No date range for {bgs_key}")

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": bgs_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":datefrom,
                                            "endDate":dateto, 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":bgs_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {bgs_key}: Missing type values")
                
                else:
                    print(f"Skipping {bgs_key}: Value is None or zero")

        #Promotion Support
        print("Promotion Support List: ", promotion_support_list)

        # Define the promotion fields to look for
        promotion_fields = [
            "middle_year_big_sales_value", "top_brand_value", "anniversary_value",
            "gawai_value", "anniversary_sales_value", "chinese_new_year_sales_value",
            "hari_raya_sales_value", "christmas_sales_value", "promotion_commission_value"
        ]

        for promotion in promotion_support_list:
            print("Processing Promotion Support: ", promotion.refno)

            for promotion_key in promotion_fields:
                promotion_value = getattr(promotion, promotion_key, None)
                if promotion_value is not None and promotion_value > 0.0:
                    print(f"Key: {promotion_key}, Value: {promotion_value}")

                    promotion_type_key = promotion_key.replace('_value', '_type')
                    promotion_value_type_key = promotion_key.replace('_value', '_value_type')

                    promotion_type_value = getattr(promotion, promotion_type_key, None)
                    promotion_value_type_value = getattr(promotion, promotion_value_type_key, None)

                    if promotion_type_value is not None and promotion_value_type_value is not None:
                        print("Promotion Value: ", promotion_value)
                        print("Promotion Type Key: ", promotion_type_key)
                        print("Promotion Type Value: ", promotion_type_value)
                        print("Promotion Value Type Key: ", promotion_value_type_key)
                        print("Promotion Value Type Value: ", promotion_value_type_value)

                        q_type = 'gr_gross_sum' if promotion_value_type_value == 'GPV' else 'gr_net_sum' if promotion_value_type_value == 'NPV' else 'Monthly' if promotion_value_type_value == 'Monthly' else 'Yearly' if promotion_value_type_value == 'Yearly' else 'unknown'

                        label = promotion_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)

                        # Date range fields
                        date_from_key = promotion_key.replace('_value', '_date_from')
                        date_to_key = promotion_key.replace('_value', '_date_to')
                        date_from = getattr(promotion, date_from_key, None)
                        date_to = getattr(promotion, date_to_key, None)

                        if date_from and date_to:
                            print(f"There is date range for {promotion_key}")

                            promotion_from = datetime.strptime(date_from, '%Y-%m-%d')
                            promotion_to = datetime.strptime(date_to, '%Y-%m-%d')

                            check_daterange = daterange_condition(label, cal_date, date_from, date_to)

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": promotion_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":check_daterange['date_from'],
                                            "endDate":check_daterange['date_to'], 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":promotion_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)
                        else:
                            print(f"No date range for {promotion_key}")

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": promotion_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":datefrom,
                                            "endDate":dateto, 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":promotion_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {promotion_key}: Missing type values")
                
                else:
                    print(f"Skipping {promotion_key}: Value is None or zero")

        #Marketing Support
        print("Marketing Support List: ", marketing_support_list)

        # Define the marketing fields to look for
        marketing_fields = [
            "packaging_fee_value", "loyalty_program_value", "anniversary_event_value",
            "crm_event_value", "marketing_event_value", "concourse_event_value"
        ]

        for marketing in marketing_support_list:
            print("Processing Marketing Support: ", marketing.refno)

            for marketing_key in marketing_fields:
                marketing_value = getattr(marketing, marketing_key, None)
                if marketing_value is not None and marketing_value > 0.0:
                    print(f"Key: {marketing_key}, Value: {marketing_value}")

                    marketing_type_key = marketing_key.replace('_value', '_type')
                    marketing_value_type_key = marketing_key.replace('_value', '_value_type')

                    marketing_type_value = getattr(marketing, marketing_type_key, None)
                    marketing_value_type_value = getattr(marketing, marketing_value_type_key, None)

                    if marketing_type_value is not None and marketing_value_type_value is not None:
                        print("Marketing Value: ", marketing_value)
                        print("Marketing Type Key: ", marketing_type_key)
                        print("Marketing Type Value: ", marketing_type_value)
                        print("Marketing Value Type Key: ", marketing_value_type_key)
                        print("Marketing Value Type Value: ", marketing_value_type_value)

                        q_type = 'gr_gross_sum' if marketing_value_type_value == 'GPV' else 'gr_net_sum' if marketing_value_type_value == 'NPV' else 'Monthly' if marketing_value_type_value == 'Monthly' else 'Yearly' if marketing_value_type_value == 'Yearly' else 'unknown'

                        label = marketing_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label)

                        # Date range fields
                        date_from_key = marketing_key.replace('_value', '_date_from')
                        date_to_key = marketing_key.replace('_value', '_date_to')
                        date_from = getattr(marketing, date_from_key, None)
                        date_to = getattr(marketing, date_to_key, None)

                        if date_from and date_to:
                            print(f"There is date range for {marketing_key}")

                            marketing_from = datetime.strptime(date_from, '%Y-%m-%d')
                            marketing_to = datetime.strptime(date_to, '%Y-%m-%d')

                            check_daterange = daterange_condition(label, cal_date, date_from, date_to)

                            # Determine datefrom1 and dateto1 based on cal_date in relation to marketing_from and marketing_to
                            if marketing_from <= cal_date <= marketing_to:
                                datefrom1 = cal_date.replace(day=1).strftime('%Y-%m-%d')
                                dateto1 = str(last_day_of_month(cal_date.date()))
                            elif cal_date > marketing_to:
                                datefrom1 = marketing_to.strftime('%Y-%m-%d')
                                dateto1 = marketing_to.strftime('%Y-%m-%d')
                            else:
                                datefrom1 = '2099-12-01'
                                dateto1 = '2099-12-31'

                            print(f"label: {label}, datefrom1: {datefrom1}, dateto1: {dateto1}")

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": marketing_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":check_daterange['date_from'],
                                            "endDate":check_daterange['date_to'], 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":marketing_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)
                        else:
                            print(f"No date range for {marketing_key}")

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": marketing_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":datefrom,
                                            "endDate":dateto, 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":marketing_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {marketing_key}: Missing type values")
                
                else:
                    print(f"Skipping {marketing_key}: Value is None or zero")

        #E_Commerce Support
        print("E-Commerce List: ", e_commerce_support_list)

        # Define the e-commerce fields to look for
        e_commerce_fields = [
            "e_commerce_sales_value", "system_setup_n_maintenance_value", "digital_communication_value",
            "social_media_post_value", "market_place_event_value"
        ]

        for e_commerce in e_commerce_support_list:
            print("Processing E-Commerce Support: ", e_commerce.refno)

            for e_commerce_key in e_commerce_fields:
                e_commerce_value = getattr(e_commerce, e_commerce_key, None)
                if e_commerce_value is not None and e_commerce_value > 0.0:
                    print(f"Key: {e_commerce_key}, Value: {e_commerce_value}")

                    e_commerce_type_key = e_commerce_key.replace('_value', '_type')
                    e_commerce_value_type_key = e_commerce_key.replace('_value', '_value_type')

                    e_commerce_type_value = getattr(e_commerce, e_commerce_type_key, None)
                    e_commerce_value_type_value = getattr(e_commerce, e_commerce_value_type_key, None)

                    if e_commerce_type_value is not None and e_commerce_value_type_value is not None:
                        print("E-Commerce Value: ", e_commerce_value)
                        print("E-Commerce Type Key: ", e_commerce_type_key)
                        print("E-Commerce Type Value: ", e_commerce_type_value)
                        print("E-Commerce Value Type Key: ", e_commerce_value_type_key)
                        print("E-Commerce Value Type Value: ", e_commerce_value_type_value)

                        q_type = 'gr_gross_sum' if e_commerce_value_type_value == 'GPV' else 'gr_net_sum' if e_commerce_value_type_value == 'NPV' else 'Monthly' if e_commerce_value_type_value == 'Monthly' else 'Yearly' if e_commerce_value_type_value == 'Yearly' else 'unknown'

                        label = e_commerce_key.replace('_value', '').replace('_', ' ').title()

                        print("Q Type: ", q_type)
                        print("Label: ", label) 

                        # Date range fields
                        date_from_key = e_commerce_key.replace('_value', '_date_from')
                        date_to_key = e_commerce_key.replace('_value', '_date_to')
                        date_from = getattr(e_commerce, date_from_key, None)
                        date_to = getattr(e_commerce, date_to_key, None)

                        if date_from and date_to:
                            print(f"There is date range for {e_commerce_key}")

                            e_commerce_from = datetime.strptime(date_from, '%Y-%m-%d')
                            e_commerce_to = datetime.strptime(date_to, '%Y-%m-%d')

                            check_daterange = daterange_condition(label, cal_date, date_from, date_to)

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": e_commerce_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":check_daterange['date_from'],
                                            "endDate":check_daterange['date_to'], 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":e_commerce_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }

                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)
                        else:
                            print(f"No date range for {e_commerce_key}")

                            calmethod = 'sum_method'

                            if calmethod == 'sum_method': 
                                    data = {
                                            "customer_guid":customer_guid, 
                                            "refno":result_1.refno, 
                                            "code":result_1.supplier_code, 
                                            "name":result_1.supplier_name, 
                                            "prefix1": e_commerce_type_value,
                                            "type":q_type,  
                                            "label":label, 
                                            "startDate":datefrom,
                                            "endDate":dateto, 
                                            "outlet" : outlet,
                                            "brand": brands,
                                            "supcode":supcode,
                                            "bf_amount":e_commerce_value,
                                            "rebate_method":[
                                            {
                                                "range":0,
                                                "type":'%',
                                                "value":0
                                            } 
                                            ]
                                        }
 
                            print("Data Prepared: ", data)

                            if (q_type == 'gr_gross_sum') or (q_type == 'gr_net_sum'):
                                # To calculate gr_sum
                                result = rims_data_functions.gr_sum(data)
                                print("Result: ", result)
                                
                                if result['status'] == live_mode:
                                    calval_method = 'non_tier'
                                    print("Calling create_inv_header_child with calval_method:", calval_method)
                                    print("Data:", data)
                                    print("Result:", result)
                                    
                                    add_data = create_inv_header_child(data, customer_guid, result, calval_method)
                                    print("Function executed successfully with result:", add_data)
                                else:
                                    error_log(list_guid, 'check_tta', data, result)

                    else:
                        print(f"Skipping {e_commerce_key}: Missing type values")
                
                else:
                    print(f"Skipping {e_commerce_key}: Value is None or zero")

        # Handling the case where result might be None
        if result is not None:
            result_status = result['status']
            data = {
                "status": result_status,
                "message": list_guid_array,
                "retailer_guid": customer_guid
            }                    

            if result_status == False:
                return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "status": False,
                "message": "We couldn't process your request. Please ensure that all values are correctly entered and try again",
                "retailer_guid": customer_guid
            }
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def export_excel3(request,customer_guid, date_from, date_to): 
    if request.method == 'GET':   
        result_status = True

        customer_guid = str('%s'%customer_guid)
        date_from = str('%s'%date_from)
        date_to = str('%s'%date_to) 
        title = customer_guid+'_'+date_from+'_'+date_to
        
        
        output =  BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Some Data')

        workbook.close()

        # create a response
        response = HttpResponse(content_type='application/vnd.ms-excel')

        # tell the browser what the file is named
        response['Content-Disposition'] = 'attachment;filename="'+title+'.xlsx"'

        # put the spreadsheet data into the response
        response.write(output.getvalue())

        # return the response
        return response 
        data = {
            "status": result_status,
            "message": customer_guid,
            "retailer_guid": customer_guid
        }
        #return data
        #print(result['status'])
        if result_status == False:
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def export_excel_old(request,customer_guid, date_from, date_to): 
    bgs_data = []
    customer_guid = str('%s'%customer_guid)
    date_from = str('%s'%date_from)
    date_to = str('%s'%date_to) 
    title = customer_guid+'_'+date_from+'_'+date_to
    
    #combine 2 list together
    # data3 = [{'refno': 'EVRTTA20030029', 'bill_supp_code': 'H0124', 'bill_supp_name': 'HARRISONS SARAWAK SDN. BHD.', 'negotiation_year': 2022, 'tta_period_from': '2022-01-01', 'tta_period_to': '2022-12-31'}, {'refno': 'EVRTTA20030032', 'bill_supp_code': 'A0048-A', 'bill_supp_name': 'A. CLOUET & CO. (KL) SDN BHD.', 'negotiation_year': 2022, 'tta_period_from': '2022-01-01', 'tta_period_to': '2099-12-30'}, {'refno': 'EVRTTA20030033', 'bill_supp_code': 'A0085', 'bill_supp_name': 'ANTARES ENTERPRISE', 'negotiation_year': 2022, 'tta_period_from': '2022-01-01', 'tta_period_to': '2099-12-30'}, {'refno': 'EVRTTA20030034', 'bill_supp_code': 'M0098-A', 'bill_supp_name': 'MEIZON PACIFIC (MP) SDN BHD - SOLEN & TORKU', 'negotiation_year': 2022, 'tta_period_from': '2022-01-01', 'tta_period_to': '2022-12-31'}, {'refno': 'EVRTTA20030036', 'bill_supp_code': 'H0145-A', 'bill_supp_name': 'HM TRACK DEAL SDN. BHD - THREE TEA', 'negotiation_year': 2022, 'tta_period_from': '2022-01-01', 'tta_period_to': '2022-12-31'}]
    # data_1ist = list(TtaList.objects.filter(customer_guid=customer_guid).
    #                 values('returnable'
    #                         ,'trading_type' 
    #         ).order_by('refno'))[:5]
    # for count,i in enumerate(data3):  
    #     for key, value  in data_1ist[count].items():  
    #         data3[count][key] = data_1ist[count][key]

    
    
    data = list(TtaList.objects.filter(customer_guid=customer_guid).
                    values('refno'
                            ,'bill_supp_code'
                            ,'bill_supp_name' 
                            , 'negotiation_year'
                            , 'tta_period_from'
                            , 'tta_period_to'
                            , 'returnable'
                            ,'trading_type'
                            # ,'supplier_profile'
                            # , 'purchase_n_rebates'
            ).order_by('refno'))[:5] 
    
    #print(data[supplier_profile])
    consolidate_result = []
    sp_data = []
    pnr_data = []

    pnd_data = []
    snd_data = []
    af_data = []
    # bgs_data = []
    # ps_data = []
    # ms_data = []
    # ecs_data = []
    result_1 = TtaList.objects.filter(customer_guid=customer_guid).order_by('refno')[:5]
    consolidate_result.append(result_1)   

    for count,i in enumerate(result_1):
        #supplier_profile
        query_header = result_1[count].supplier_profile
        for sp in query_header: 
            if sp['field'] == 'outlet': 
                    if sp['prefix1']['value'] != 'All':
                        val_outlet = sp['prefix2']['value']
                        #selected outlet 
                        q_outlet = RimsCpSetBranch.objects.filter(branch_guid__in=val_outlet).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
                        outlet = list(q_outlet) 
                    else:    
                        val_outlet = sp['prefix1']['value']
                        # all outlet 
                        q_outlet = RimsCpSetBranch.objects.exclude(set_active=0).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
                        outlet = list(q_outlet) 
                    
            if sp['field'] == 'exclude_outlet':
                    #use length to check empty 
                    if(len(sp['prefix1']['value']) != 0):  
                        excl_outlet = sp['prefix1']['value'] 
                        q_outlet = RimsCpSetBranch.objects.exclude(set_active=0).exclude(branch_guid__in=excl_outlet).filter(customer_guid=customer_guid).values_list('branch_code', flat=True)
                        outlet = list(q_outlet)

            if sp['field'] == 'trading_brand':
                    if(len(sp['prefix1']['value']) != 0):
                        val_brand = sp['prefix1']['value'] 
                        q_brand = RimsBrand.objects.filter(brand_guid__in=val_brand).filter(customer_guid=customer_guid).values_list('code', flat=True)
                        brand = list(q_brand)
                    else: 
                        brand = sp['prefix1']['value'] 
                    #print(brand)
                    
        supplier_profile = {
                "outlet": outlet, 
                "brand": brand
            }
        sp_data.append(supplier_profile)

        #purchase_n_rebates

        #payment_n_discount 
        #start
        query_pnd = result_1[count].payment_n_discount 
        for pnd in query_pnd: 
            try:
                if(pnd['calMethod'] == 'Method1'):
                    try:
                        #force something hopefully wont kena
                        if(pnd['input1'] != 'makesureifgotdata'):
                            field = pnd['field']
                            label = pnd['label']
                            input1 = pnd['input1']
                            prefix1 = pnd['prefix1']['value']
                            
                            radio = pnd['radio1']['value']

                            payment_n_discount = {
                                field: pnd['input1'], 
                                field+"_prefix1": prefix1,
                                'count': count
                                } 
                            pnd_data.append(payment_n_discount) 
                            
                    except KeyError:
                        payment_n_discount = {
                                pnd['field']: "0", 
                                pnd['field']+"_prefix1": pnd['prefix1']['value'],
                                'count': count
                            }
                        pnd_data.append(payment_n_discount)  
                    
            except KeyError: 
                pass 

        result = {}  
        for d in pnd_data:
            key = d['count'] 
            if key not in result:
                result[key] = {}
            result[key].update(d)     

        pnd = list(result.values())
        #end
        
        #stock_n_deliveries
        query_snd = result_1[count].stock_n_deliveries 
        for snd in query_snd: 
            try:
                if(snd['calMethod'] == 'Method1'):
                    try:
                        #force something hopefully wont kena
                        if(snd['input1'] != 'makesureifgotdata'):
                            field = snd['field']
                            label = snd['label']
                            input1 = snd['input1']
                            prefix1 = snd['prefix1']['value']
                            
                            radio = snd['radio1']['value']

                            stock_n_deliveries = {
                                field: snd['input1'], 
                                field+"_prefix1": prefix1,
                                'count': count
                                } 
                            snd_data.append(stock_n_deliveries) 
                            
                    except KeyError:
                        stock_n_deliveries = {
                                snd['field']: "0", 
                                snd['field']+"_prefix1": snd['prefix1']['value'],
                                'count': count
                            }
                        snd_data.append(stock_n_deliveries)  
                    
            except KeyError: 
                pass 

        result = {}  
        for d in snd_data:
            key = d['count'] 
            if key not in result:
                result[key] = {}
            result[key].update(d)     

        snd = list(result.values())
        #end

        #administration_fees
        query_af = result_1[count].administration_fees 
        for af in query_af: 
            try:
                if(af['calMethod'] == 'Method1'):
                    try:
                        #force something hopefully wont kena
                        if(af['input1'] != 'makesureifgotdata'):
                            field = af['field']
                            label = af['label']
                            input1 = af['input1']
                            prefix1 = af['prefix1']['value']
                            
                            radio = af['radio1']['value']

                            administration_fees = {
                                field: af['input1'], 
                                field+"_prefix1": prefix1,
                                'count': count
                                } 
                            af_data.append(administration_fees) 
                            
                    except KeyError:
                        administration_fees = {
                                af['field']: "0", 
                                af['field']+"_prefix1": af['prefix1']['value'],
                                'count': count
                            }
                        af_data.append(administration_fees)  
                    
            except KeyError: 
                pass 

        result = {}  
        for d in af_data:
            key = d['count'] 
            if key not in result:
                result[key] = {}
            result[key].update(d)     

        af = list(result.values())

        #business_growth_support
        query_bgs = result_1[count].business_growth_support 
        for bgs in query_bgs: 
            try:
                if(bgs['calMethod'] == 'Method1'):
                    try:
                        #force something hopefully wont kena
                        if(bgs['input1'] != 'makesureifgotdata'):
                            field = bgs['field']
                            label = bgs['label']
                            input1 = bgs['input1']
                            prefix1 = bgs['prefix1']['value']
                            
                            radio = bgs['radio1']['value']

                            administration_fees = {
                                field: bgs['input1'], 
                                field+"_prefix1": prefix1,
                                'count': count
                                } 
                            bgs_data.append(administration_fees) 
                            
                    except KeyError:
                        administration_fees = {
                                bgs['field']: "0", 
                                bgs['field']+"_prefix1": bgs['prefix1']['value'],
                                'count': count
                            }
                        bgs_data.append(administration_fees)  
                    
            except KeyError: 
                pass 

        result = {}  
        for d in bgs_data:
            key = d['count'] 
            if key not in result:
                result[key] = {}
            result[key].update(d)     

        bgs = list(result.values())
    
    for count,i in enumerate(data):  
        for key, value  in sp_data[count].items():  
            data[count][key] = sp_data[count][key]

    for count,i in enumerate(data):  
        for key, value  in pnd[count].items():  
            data[count][key] = pnd[count][key]

    for count,i in enumerate(data):  
        for key, value  in snd[count].items():  
            data[count][key] = snd[count][key]

    for count,i in enumerate(data):  
        for key, value  in af[count].items():  
            data[count][key] = af[count][key]            
    
    # for count,i in enumerate(data):  
    #     for key, value  in pnr_data[count].items():  
    #         data[count][key] = pnr_data[count][key]
    
    return Response(data, status=status.HTTP_200_OK)

    with BytesIO() as b:
        # Use the StringIO object as the filehandle.  
        df = pd.DataFrame(data) 

        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        # Set up the Http response.
        filename = title+'.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


    data = {
            "status": True,
            "message": customer_guid,
            "retailer_guid": customer_guid
        } 
    return Response(data, status=status.HTTP_200_OK)

def format_numeric_columns(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        # Format numbers to 2 decimal places, except those in lists
        df[col] = df[col].apply(lambda x: f"{x:.2f}" if not pd.isna(x) and not isinstance(x, list) else "")
    return df

@api_view(['GET'])
def export_excel(request,customer_guid, date_from, date_to):
    print("Start Export Excel Api")
    newlist=[]
    run=0

    # result=TtaList.objects.all()
    
    customer_guid = str('%s'%customer_guid)
    date_from = str('%s'%date_from)
    date_to = str('%s'%date_to) 
    title = customer_guid+'_'+date_from+'_'+date_to 
    
    result = TtaList.objects.filter(customer_guid=customer_guid).values('refno'
                            ,'bill_supp_code'
                            ,'bill_supp_name' 
                            , 'negotiation_year'
                            , 'tta_period_from'
                            , 'tta_period_to'
                            , 'returnable'
                            , 'trading_type'
                            , 'trading_brand__brand_guid'
                            , 'outlet_type'
                            , 'outlet__branch_guid'
                            , 'exclude_outlet__branch_guid'
                            #Purchase N Rebates
                            , 'purchase_n_rebates__unconditional_rebate_value'
                            , 'purchase_n_rebates__unconditional_rebate_type'
                            , 'purchase_n_rebates__unconditional_rebate_value_type'
                            , 'purchase_n_rebates__commission_value'
                            , 'purchase_n_rebates__commission_type'
                            , 'purchase_n_rebates__commission_value_type'
                            , 'purchase_n_rebates__auto_replenishment_rebate_value'
                            , 'purchase_n_rebates__auto_replenishment_rebate_type'
                            , 'purchase_n_rebates__auto_replenishment_rebate_value_type'
                            , 'purchase_n_rebates__monthly_discount_value'
                            , 'purchase_n_rebates__monthly_discount_type'
                            , 'purchase_n_rebates__monthly_discount_value_type'
                            , 'purchase_n_rebates__target_period_type'
                            , 'purchase_n_rebates__target_purchase_tier_1_value1'
                            , 'purchase_n_rebates__target_purchase_tier_1_value2'
                            , 'purchase_n_rebates__target_purchase_tier_1_type1'
                            , 'purchase_n_rebates__target_purchase_tier_1_type2'
                            , 'purchase_n_rebates__target_purchase_tier_1_value_type'
                            , 'purchase_n_rebates__target_purchase_tier_2_value1'
                            , 'purchase_n_rebates__target_purchase_tier_2_value2'
                            , 'purchase_n_rebates__target_purchase_tier_2_type1'
                            , 'purchase_n_rebates__target_purchase_tier_2_type2'
                            , 'purchase_n_rebates__target_purchase_tier_2_value_type'
                            , 'purchase_n_rebates__target_purchase_tier_3_value1'
                            , 'purchase_n_rebates__target_purchase_tier_3_value2'
                            , 'purchase_n_rebates__target_purchase_tier_3_type1'
                            , 'purchase_n_rebates__target_purchase_tier_3_type2'
                            , 'purchase_n_rebates__target_purchase_tier_3_value_type'
                            , 'purchase_n_rebates__target_growth_tier_1_value1'
                            , 'purchase_n_rebates__target_growth_tier_1_value2'
                            , 'purchase_n_rebates__target_growth_tier_1_type1'
                            , 'purchase_n_rebates__target_growth_tier_1_type2'
                            , 'purchase_n_rebates__target_growth_tier_1_type3'
                            , 'purchase_n_rebates__target_growth_tier_1_type4'
                            , 'purchase_n_rebates__target_growth_tier_1_value_type'
                            , 'purchase_n_rebates__target_growth_tier_2_value1'
                            , 'purchase_n_rebates__target_growth_tier_2_value2'
                            , 'purchase_n_rebates__target_growth_tier_2_type1'
                            , 'purchase_n_rebates__target_growth_tier_2_type2'
                            , 'purchase_n_rebates__target_growth_tier_2_type3'
                            , 'purchase_n_rebates__target_growth_tier_2_type4'
                            , 'purchase_n_rebates__target_growth_tier_2_value_type'
                            , 'purchase_n_rebates__target_growth_tier_3_value1'
                            , 'purchase_n_rebates__target_growth_tier_3_value2'
                            , 'purchase_n_rebates__target_growth_tier_3_type1'
                            , 'purchase_n_rebates__target_growth_tier_3_type2'
                            , 'purchase_n_rebates__target_growth_tier_3_type3'
                            , 'purchase_n_rebates__target_growth_tier_3_type4'
                            , 'purchase_n_rebates__target_growth_tier_3_value_type'
                            #Payment N Discount
                            , 'payment_n_discount__payment_terms_type'
                            , 'payment_n_discount__early_payment_terms_type'
                            , 'payment_n_discount__early_payment_terms_value'
                            , 'payment_n_discount__early_payment_discount_value'
                            , 'payment_n_discount__early_payment_discount_type'
                            , 'payment_n_discount__early_payment_discount_value_type'
                            , 'payment_n_discount__prompt_payment_discount_value'
                            , 'payment_n_discount__prompt_payment_discount_type'
                            , 'payment_n_discount__prompt_payment_discount_value_type'
                            #Stock N Deliveries
                            , 'stock_n_deliveries__cross_docking_allowance_value'
                            , 'stock_n_deliveries__cross_docking_allowance_type'
                            , 'stock_n_deliveries__cross_docking_allowance_value_type'
                            , 'stock_n_deliveries__conventional_flow_thru_allowance_value'
                            , 'stock_n_deliveries__conventional_flow_thru_allowance_type'
                            , 'stock_n_deliveries__conventional_flow_thru_allowance_value_type'
                            , 'stock_n_deliveries__shrinkage_pilferage_allowance_value'
                            , 'stock_n_deliveries__shrinkage_pilferage_allowance_type'
                            , 'stock_n_deliveries__shrinkage_pilferage_allowance_value_type'
                            , 'stock_n_deliveries__non_returnable_goods_allowance_value'
                            , 'stock_n_deliveries__non_returnable_goods_allowance_type'
                            , 'stock_n_deliveries__non_returnable_goods_allowance_value_type'
                            , 'stock_n_deliveries__east_malaysia_orders_allowance_value'
                            , 'stock_n_deliveries__east_malaysia_orders_allowance_type'
                            , 'stock_n_deliveries__east_malaysia_orders_allowance_value_type'
                            , 'stock_n_deliveries__damage_good_allowance_value'
                            , 'stock_n_deliveries__damage_good_allowance_type'
                            , 'stock_n_deliveries__damage_good_allowance_value_type'
                            , 'stock_n_deliveries__non_compliance_packaging_allowance_value'
                            , 'stock_n_deliveries__non_compliance_packaging_allowance_type'
                            , 'stock_n_deliveries__non_compliance_packaging_allowance_value_type'
                            , 'stock_n_deliveries__purchase_order_fulfillment_value'
                            , 'stock_n_deliveries__purchase_order_fulfillment_type'
                            , 'stock_n_deliveries__purchase_order_fulfillment_value_type'
                            , 'stock_n_deliveries__unfulfilled_penalty_value'
                            , 'stock_n_deliveries__unfulfilled_penalty_type'
                            , 'stock_n_deliveries__unfulfilled_penalty_value_type'
                            , 'stock_n_deliveries__lost_of_profit_penalty_value'
                            , 'stock_n_deliveries__lost_of_profit_penalty_type'
                            , 'stock_n_deliveries__lost_of_profit_penalty_value_type'
                            , 'stock_n_deliveries__purchase_order_lead_time_value'
                            , 'stock_n_deliveries__purchase_order_lead_time_type'
                            , 'stock_n_deliveries__purchase_order_lead_time_value_type'
                            , 'stock_n_deliveries__lead_time_penalty_value'
                            , 'stock_n_deliveries__lead_time_penalty_type'
                            , 'stock_n_deliveries__lead_time_penalty_value_type'
                            , 'stock_n_deliveries__ullarge_value'
                            , 'stock_n_deliveries__ullarge_type'
                            , 'stock_n_deliveries__ullarge_value_type'
                            , 'stock_n_deliveries__target_service_level_value'
                            , 'stock_n_deliveries__target_service_level_type'
                            , 'stock_n_deliveries__target_service_level_value_type'
                            , 'stock_n_deliveries__target_service_level_unfulfilled_penalty_value'
                            , 'stock_n_deliveries__target_service_level_unfulfilled_penalty_type'
                            , 'stock_n_deliveries__target_service_level_unfulfilled_penalty_value_type'
                            #Administration Fees
                            , 'administration_fees__account_administration_fee_value'
                            , 'administration_fees__account_administration_fee_type'
                            , 'administration_fees__account_administration_fee_value_type'
                            , 'administration_fees__product_registration_fee_value'
                            , 'administration_fees__product_registration_fee_type'
                            , 'administration_fees__product_registration_fee_value_type'
                            , 'administration_fees__sku_replacement_value'
                            , 'administration_fees__sku_replacement_type'
                            , 'administration_fees__sku_replacement_value_type'
                            , 'administration_fees__new_line_fee_value'
                            , 'administration_fees__new_line_fee_type'
                            , 'administration_fees__new_line_fee_value_type'
                            , 'administration_fees__new_item_listing_value'
                            , 'administration_fees__new_item_listing_type'
                            , 'administration_fees__new_item_listing_value_type'
                            , 'administration_fees__new_item_first_order_discount_value1'
                            , 'administration_fees__new_item_first_order_discount_value2'
                            , 'administration_fees__new_item_first_order_discount_type1'
                            , 'administration_fees__new_item_first_order_discount_type2'
                            , 'administration_fees__new_item_first_order_discount_value_type'
                            , 'administration_fees__change_of_purchase_type_value'
                            , 'administration_fees__change_of_purchase_type_type'
                            , 'administration_fees__change_of_purchase_type_value_type'
                            , 'administration_fees__maintenance_of_vendor_information_value'
                            , 'administration_fees__maintenance_of_vendor_information_type'
                            , 'administration_fees__maintenance_of_vendor_information_value_type'
                            , 'administration_fees__new_vcr_barcode_value'
                            , 'administration_fees__new_vcr_barcode_type'
                            , 'administration_fees__new_vcr_barcode_value_type'
                            #Business Growth Support
                            , 'business_growth_support__category_development_fund_value'
                            , 'business_growth_support__category_development_fund_type'
                            , 'business_growth_support__category_development_fund_value_type'
                            , 'business_growth_support__business_development_fund_value'
                            , 'business_growth_support__business_development_fund_type'
                            , 'business_growth_support__business_development_fund_value_type'
                            , 'business_growth_support__data_sharing_fee_value'
                            , 'business_growth_support__data_sharing_fee_type'
                            , 'business_growth_support__data_sharing_fee_value_type'
                            , 'business_growth_support__new_store_opening_value'
                            , 'business_growth_support__new_store_opening_type'
                            , 'business_growth_support__new_store_opening_value_type'
                            , 'business_growth_support__new_store_first_order_discount_value1'
                            , 'business_growth_support__new_store_first_order_discount_value2'
                            , 'business_growth_support__new_store_first_order_discount_type1'
                            , 'business_growth_support__new_store_first_order_discount_type2'
                            , 'business_growth_support__new_store_first_order_discount_value_type'
                            , 'business_growth_support__refurbish_store_value'
                            , 'business_growth_support__refurbish_store_type'
                            , 'business_growth_support__refurbish_store_value_type'
                            , 'business_growth_support__anniversary_sales_allowance_value'
                            , 'business_growth_support__anniversary_sales_allowance_type'
                            , 'business_growth_support__anniversary_sales_allowance_value_type'
                            , 'business_growth_support__anniversary_orders_rebate_value'
                            , 'business_growth_support__anniversary_orders_rebate_type'
                            , 'business_growth_support__anniversary_orders_rebate_value_type'
                            #Promotion Support
                            , 'promotion_support__middle_year_big_sales_value'
                            , 'promotion_support__middle_year_big_sales_type'
                            , 'promotion_support__middle_year_big_sales_value_type'
                            , 'promotion_support__top_brand_value'
                            , 'promotion_support__top_brand_type'
                            , 'promotion_support__top_brand_value_type'
                            , 'promotion_support__anniversary_value'
                            , 'promotion_support__anniversary_type'
                            , 'promotion_support__anniversary_value_type'
                            , 'promotion_support__gawai_value'
                            , 'promotion_support__gawai_type'
                            , 'promotion_support__gawai_value_type'
                            , 'promotion_support__gawai_sales_value'
                            , 'promotion_support__gawai_sales_type'
                            , 'promotion_support__gawai_sales_value_type'
                            , 'promotion_support__anniversary_sales_value'
                            , 'promotion_support__anniversary_sales_type'
                            , 'promotion_support__anniversary_sales_value_type'
                            , 'promotion_support__chinese_new_year_sales_value'
                            , 'promotion_support__chinese_new_year_sales_type'
                            , 'promotion_support__chinese_new_year_sales_value_type'
                            , 'promotion_support__hari_raya_sales_value'
                            , 'promotion_support__hari_raya_sales_type'
                            , 'promotion_support__hari_raya_sales_value_type'
                            , 'promotion_support__christmas_sales_value'
                            , 'promotion_support__christmas_sales_type'
                            , 'promotion_support__christmas_sales_value_type'
                            , 'promotion_support__promotion_commission_value'
                            , 'promotion_support__promotion_commission_type'
                            , 'promotion_support__promotion_commission_value_type'
                            #Display Incentive
                            , 'display_incentive'
                            #Marketing Support
                            , 'marketing_support__packaging_fee_value'
                            , 'marketing_support__packaging_fee_type'
                            , 'marketing_support__packaging_fee_value_type'
                            , 'marketing_support__loyalty_program_value'
                            , 'marketing_support__loyalty_program_type'
                            , 'marketing_support__loyalty_program_value_type'
                            , 'marketing_support__anniversary_event_value'
                            , 'marketing_support__anniversary_event_type'
                            , 'marketing_support__anniversary_event_value_type'
                            , 'marketing_support__crm_event_value'
                            , 'marketing_support__crm_event_type'
                            , 'marketing_support__crm_event_value_type'
                            , 'marketing_support__marketing_event_value'
                            , 'marketing_support__marketing_event_type'
                            , 'marketing_support__marketing_event_value_type'
                            , 'marketing_support__concourse_event_value'
                            , 'marketing_support__concourse_event_type'
                            , 'marketing_support__concourse_event_value_type'
                            #E-Commerce Support
                            , 'e_commerce_support__e_commerce_sales_value'
                            , 'e_commerce_support__e_commerce_sales_type'
                            , 'e_commerce_support__e_commerce_sales_value_type'
                            , 'e_commerce_support__system_setup_n_maintenance_value'
                            , 'e_commerce_support__system_setup_n_maintenance_type'
                            , 'e_commerce_support__system_setup_n_maintenance_value_type'
                            , 'e_commerce_support__digital_communication_value'
                            , 'e_commerce_support__digital_communication_type'
                            , 'e_commerce_support__digital_communication_value_type'
                            , 'e_commerce_support__social_media_post_value'
                            , 'e_commerce_support__social_media_post_type'
                            , 'e_commerce_support__social_media_post_value_type'
                            , 'e_commerce_support__market_place_event_value'
                            , 'e_commerce_support__market_place_event_type'
                            , 'e_commerce_support__market_place_event_value_type'
            ).order_by('refno') 

    # Dictionary to hold trading brands, outlet_branch and exclude_outlet_branch for each refno
    trading_brands = {}
    outlet_branch = {}
    exclude_outlet_branch = {}

    for row in result:
        refno = row['refno']
        trading_brands.setdefault(refno, set())
        outlet_branch.setdefault(refno, set())
        exclude_outlet_branch.setdefault(refno, set())

        brand_guid = row.get('trading_brand__brand_guid')
        if brand_guid:
            q_brand = RimsBrand.objects.filter(brand_guid=brand_guid, customer_guid=customer_guid).values_list('code', flat=True)
            trading_brands[refno].update(q_brand)

        branch_guid = row.get('outlet__branch_guid')
        if branch_guid:
            outlet_branch[refno].add(branch_guid)

        exclude_branch_guid = row.get('exclude_outlet__branch_guid')
        if exclude_branch_guid:
            q_branch = RimsCpSetBranch.objects.filter(branch_guid=exclude_branch_guid, customer_guid=customer_guid).values_list('branch_code', flat=True)
            exclude_outlet_branch[refno].update(q_branch)

    processed_refnos = set()

    for row in result:
        refno = row['refno']
        if refno in processed_refnos:
            continue  # Skip if this refno has already been processed

        brands = list(trading_brands.get(refno, []))
        branch_guids = list(outlet_branch.get(refno, []))
        exclude_branch = list(exclude_outlet_branch.get(refno, []))

        if row.get('outlet_type', 'default_value') == 'All':
            outlet = "All"
        elif row.get('outlet_type', 'default_value') == 'Outlet':
            q_outlet = RimsCpSetBranch.objects.filter(branch_guid__in=branch_guids, customer_guid=customer_guid).values_list('branch_code', flat=True)
            outlet = list(q_outlet)
        else:
            outlet = []

        dataset={ 
                "ref_no":refno,
                "bill_supp_code":row['bill_supp_code'],
                "bill_supp_name":row['bill_supp_name'],
                "tta_period_from":row['tta_period_from'],
                "tta_period_to":row['tta_period_to'],
                "returnable":row['returnable'],
                "trading_type":row['trading_type'],  
                "trading_brand": brands,
                "outlet": outlet,
                "exclude_outlet": exclude_branch,
                #Purchase N Rebates
                "unconditional_rebate": row['purchase_n_rebates__unconditional_rebate_value'],
                "unconditional_rebate_type": row['purchase_n_rebates__unconditional_rebate_type'],
                "unconditional_rebate_remark": row['purchase_n_rebates__unconditional_rebate_value_type'],
                "commission": row['purchase_n_rebates__commission_value'],
                "commission_type": row['purchase_n_rebates__commission_type'],
                "commission_remark": row['purchase_n_rebates__commission_value_type'],
                "auto_replenishment_rebate": row['purchase_n_rebates__auto_replenishment_rebate_value'],
                "auto_replenishment_rebate_type": row['purchase_n_rebates__auto_replenishment_rebate_type'],
                "purchase_n_rebates__auto_replenishment_rebate_remark": row['purchase_n_rebates__auto_replenishment_rebate_value_type'],
                "monthly_discount": row['purchase_n_rebates__monthly_discount_value'],
                "monthly_discount_type": row['purchase_n_rebates__monthly_discount_type'],
                "monthly_discount_remark": row['purchase_n_rebates__monthly_discount_value_type'],
                "target_period": row['purchase_n_rebates__target_period_type'],
                "target_purchase_tier_1": row['purchase_n_rebates__target_purchase_tier_1_value1'],
                "target_purchase_tier_1_type": row['purchase_n_rebates__target_purchase_tier_1_type1'],
                "target_purchase_tier_1_remark": row['purchase_n_rebates__target_purchase_tier_1_value_type'],
                "target_purchase_tier_1_rate": row['purchase_n_rebates__target_purchase_tier_1_value2'],
                "target_purchase_tier_1_rate_uom": row['purchase_n_rebates__target_purchase_tier_1_type2'],
                "target_purchase_tier_2": row['purchase_n_rebates__target_purchase_tier_2_value1'],
                "target_purchase_tier_2_type": row['purchase_n_rebates__target_purchase_tier_2_type1'],
                "target_purchase_tier_2_remark": row['purchase_n_rebates__target_purchase_tier_2_value_type'],
                "target_purchase_tier_2_rate": row['purchase_n_rebates__target_purchase_tier_2_value2'],
                "target_purchase_tier_2_rate_uom": row['purchase_n_rebates__target_purchase_tier_2_type2'],
                "target_purchase_tier_3": row['purchase_n_rebates__target_purchase_tier_3_value1'],
                "target_purchase_tier_3_type": row['purchase_n_rebates__target_purchase_tier_3_type1'],
                "target_purchase_tier_3_remark": row['purchase_n_rebates__target_purchase_tier_3_value_type'],
                "target_purchase_tier_3_rate": row['purchase_n_rebates__target_purchase_tier_3_value2'],
                "target_purchase_tier_3_rate_uom": row['purchase_n_rebates__target_purchase_tier_3_type2'],
                "target_growth_tier_1": row['purchase_n_rebates__target_growth_tier_1_value1'],
                "target_growth_tier_1_type": row['purchase_n_rebates__target_growth_tier_1_type1'],
                "target_growth_tier_1_remark": row['purchase_n_rebates__target_growth_tier_1_value_type'],
                "target_growth_tier_1_rate": row['purchase_n_rebates__target_growth_tier_1_value2'],
                "target_growth_tier_1_rate_uom": row['purchase_n_rebates__target_growth_tier_1_type2'],
                "target_growth_tier_1_division": row['purchase_n_rebates__target_growth_tier_1_type3'],
                "target_growth_tier_2": row['purchase_n_rebates__target_growth_tier_2_value1'],
                "target_growth_tier_2_type": row['purchase_n_rebates__target_growth_tier_2_type1'],
                "target_growth_tier_2_remark": row['purchase_n_rebates__target_growth_tier_2_value_type'],
                "target_growth_tier_2_rate": row['purchase_n_rebates__target_growth_tier_2_value2'],
                "target_growth_tier_2_rate_uom": row['purchase_n_rebates__target_growth_tier_2_type2'],
                "target_growth_tier_2_division": row['purchase_n_rebates__target_growth_tier_2_type3'],
                "target_growth_tier_3": row['purchase_n_rebates__target_growth_tier_3_value1'],
                "target_growth_tier_3_type": row['purchase_n_rebates__target_growth_tier_3_type1'],
                "target_growth_tier_3_remark": row['purchase_n_rebates__target_growth_tier_3_value_type'],
                "target_growth_tier_3_rate": row['purchase_n_rebates__target_growth_tier_3_value2'],
                "target_growth_tier_3_rate_uom": row['purchase_n_rebates__target_growth_tier_3_type2'],
                "target_growth_tier_3_division": row['purchase_n_rebates__target_growth_tier_3_type3'],
                #Payment N Discount
                "payment_terms": row['payment_n_discount__payment_terms_type'],
                "early_payment_terms": row['payment_n_discount__early_payment_terms_value'],
                "early_payment_terms_type": row['payment_n_discount__early_payment_terms_type'],
                "early_payment_discount": row['payment_n_discount__early_payment_discount_value'],
                "early_payment_discount_type": row['payment_n_discount__early_payment_discount_type'],
                "early_payment_discount_remark": row['payment_n_discount__early_payment_discount_value_type'],
                "prompt_payment_discount": row['payment_n_discount__prompt_payment_discount_value'],
                "prompt_payment_discount_type": row['payment_n_discount__prompt_payment_discount_type'],
                "prompt_payment_discount_remark": row['payment_n_discount__prompt_payment_discount_value_type'],
                #Stock N Deliveries
                "cross_docking_allowance": row['stock_n_deliveries__cross_docking_allowance_value'],
                "cross_docking_allowance_type": row['stock_n_deliveries__cross_docking_allowance_type'],
                "cross_docking_allowance_remark": row['stock_n_deliveries__cross_docking_allowance_value_type'],
                "conventional_flow_thru_allowance": row['stock_n_deliveries__conventional_flow_thru_allowance_value'],
                "conventional_flow_thru_allowance_type": row['stock_n_deliveries__conventional_flow_thru_allowance_type'],
                "conventional_flow_thru_allowance_remark": row['stock_n_deliveries__conventional_flow_thru_allowance_value_type'],
                "shrinkage_pilferage_allowance": row['stock_n_deliveries__shrinkage_pilferage_allowance_value'],
                "shrinkage_pilferage_allowance_type": row['stock_n_deliveries__shrinkage_pilferage_allowance_type'],
                "shrinkage_pilferage_allowance_remark": row['stock_n_deliveries__shrinkage_pilferage_allowance_value_type'],
                "non_returnable_goods_allowance": row['stock_n_deliveries__non_returnable_goods_allowance_value'],
                "non_returnable_goods_allowance_type": row['stock_n_deliveries__non_returnable_goods_allowance_type'],
                "non_returnable_goods_allowance_remark": row['stock_n_deliveries__non_returnable_goods_allowance_value_type'],
                "east_malaysia_orders_allowance": row['stock_n_deliveries__east_malaysia_orders_allowance_value'],
                "east_malaysia_orders_allowance_type": row['stock_n_deliveries__east_malaysia_orders_allowance_type'],
                "east_malaysia_orders_allowance_remark": row['stock_n_deliveries__east_malaysia_orders_allowance_value_type'],
                "damage_good_allowance": row['stock_n_deliveries__damage_good_allowance_value'],
                "damage_good_allowance_type": row['stock_n_deliveries__damage_good_allowance_type'],
                "damage_good_allowance_remark": row['stock_n_deliveries__damage_good_allowance_value_type'],
                "non_compliance_packaging_allowance": row['stock_n_deliveries__non_compliance_packaging_allowance_value'],
                "non_compliance_packaging_allowance_type": row['stock_n_deliveries__non_compliance_packaging_allowance_type'],
                "non_compliance_packaging_allowance_remark": row['stock_n_deliveries__non_compliance_packaging_allowance_value_type'],
                "purchase_order_fulfillment": row['stock_n_deliveries__purchase_order_fulfillment_value'],
                "purchase_order_fulfillment_type": row['stock_n_deliveries__purchase_order_fulfillment_type'],
                "purchase_order_fulfillment_remark": row['stock_n_deliveries__purchase_order_fulfillment_value_type'],
                "unfulfilled_penalty": row['stock_n_deliveries__unfulfilled_penalty_value'],
                "unfulfilled_penalty_type": row['stock_n_deliveries__unfulfilled_penalty_type'],
                "unfulfilled_penalty_remark": row['stock_n_deliveries__unfulfilled_penalty_value_type'],
                "lost_of_profit_penalty": row['stock_n_deliveries__lost_of_profit_penalty_value'],
                "lost_of_profit_penalty_type": row['stock_n_deliveries__lost_of_profit_penalty_type'],
                "lost_of_profit_penalty_remark": row['stock_n_deliveries__lost_of_profit_penalty_value_type'],
                "purchase_order_lead_time": row['stock_n_deliveries__purchase_order_lead_time_value'],
                "purchase_order_lead_time_type": row['stock_n_deliveries__purchase_order_lead_time_type'],
                "purchase_order_lead_time_remark": row['stock_n_deliveries__purchase_order_lead_time_value_type'],
                "lead_time_penalty": row['stock_n_deliveries__lead_time_penalty_value'],
                "lead_time_penalty_type": row['stock_n_deliveries__lead_time_penalty_type'],
                "lead_time_penalty_remark": row['stock_n_deliveries__lead_time_penalty_value_type'],
                "ullarge": row['stock_n_deliveries__ullarge_value'],
                "ullarge_type": row['stock_n_deliveries__ullarge_type'],
                "ullarge_remark": row['stock_n_deliveries__ullarge_value_type'],
                "target_service_level": row['stock_n_deliveries__target_service_level_value'],
                "target_service_level_type": row['stock_n_deliveries__target_service_level_type'],
                "target_service_level_remark": row['stock_n_deliveries__target_service_level_value_type'],
                "target_service_level_unfulfilled_penalty": row['stock_n_deliveries__target_service_level_unfulfilled_penalty_value'],
                "target_service_level_unfulfilled_penalty_type": row['stock_n_deliveries__target_service_level_unfulfilled_penalty_type'],
                "target_service_level_unfulfilled_penalty_remark": row['stock_n_deliveries__target_service_level_unfulfilled_penalty_value_type'],
                #Administration Fees
                "account_administration_fee": row['administration_fees__account_administration_fee_value'],
                "account_administration_fee_type": row['administration_fees__account_administration_fee_type'],
                "account_administration_fee_remark": row['administration_fees__account_administration_fee_value_type'],  
                "product_registration_fee": row['administration_fees__product_registration_fee_value'],
                "product_registration_fee_type": row['administration_fees__product_registration_fee_type'],
                "product_registration_fee_remark": row['administration_fees__product_registration_fee_value_type'],     
                "sku_replacement": row['administration_fees__sku_replacement_value'],
                "sku_replacement_type": row['administration_fees__sku_replacement_type'],
                "sku_replacement_remark": row['administration_fees__sku_replacement_value_type'],     
                "new_line_fee": row['administration_fees__new_line_fee_value'],
                "new_line_fee_type": row['administration_fees__new_line_fee_type'],
                "new_line_fee_remark": row['administration_fees__new_line_fee_value_type'],           
                "new_item_listing": row['administration_fees__new_item_listing_value'],
                "new_item_listing_type": row['administration_fees__new_item_listing_type'],
                "new_item_listing_remark": row['administration_fees__new_item_listing_value_type'],           
                "new_item_first_order_discount": row['administration_fees__new_item_first_order_discount_value1'],
                "new_item_first_order_discount_type": row['administration_fees__new_item_first_order_discount_type1'],
                "new_item_first_order_discount_remark": row['administration_fees__new_item_first_order_discount_value_type'],  
                "change_of_purchase_type": row['administration_fees__change_of_purchase_type_value'],
                "change_of_purchase_type_type": row['administration_fees__change_of_purchase_type_type'],
                "change_of_purchase_type_remark": row['administration_fees__change_of_purchase_type_value_type'],       
                "maintenance_of_vendor_information_type": row['administration_fees__maintenance_of_vendor_information_value'],
                "maintenance_of_vendor_information_type": row['administration_fees__maintenance_of_vendor_information_type'],
                "maintenance_of_vendor_information_remark": row['administration_fees__maintenance_of_vendor_information_value_type'],   
                "new_vendor_creation_request_by_existing_vendor_barcode": row['administration_fees__new_vcr_barcode_value'],
                "new_vendor_creation_request_by_existing_vendor_barcode_type": row['administration_fees__new_vcr_barcode_type'],
                "new_vendor_creation_request_by_existing_vendor_barcode_remark": row['administration_fees__new_vcr_barcode_value_type'], 
                #Business Growth Support
                "category_development_fund": row['business_growth_support__category_development_fund_value'],
                "category_development_fund_type": row['business_growth_support__category_development_fund_type'],
                "category_development_fund_value_type": row['business_growth_support__category_development_fund_value_type'],
                "business_development_fund": row['business_growth_support__business_development_fund_value'],
                "business_development_fund_type": row['business_growth_support__business_development_fund_type'],
                "business_development_fund_value_type": row['business_growth_support__business_development_fund_value_type'],
                "data_sharing_fee": row['business_growth_support__data_sharing_fee_value'],
                "data_sharing_fee_type": row['business_growth_support__data_sharing_fee_type'],
                "data_sharing_fee_value_type": row['business_growth_support__data_sharing_fee_value_type'],
                "new_store_opening": row['business_growth_support__new_store_opening_value'],
                "new_store_opening_type": row['business_growth_support__new_store_opening_type'],
                "new_store_opening_value_type": row['business_growth_support__new_store_opening_value_type'],
                "new_store_first_order_discount": row['business_growth_support__new_store_first_order_discount_value1'],
                "new_store_first_order_discount_type": row['business_growth_support__new_store_first_order_discount_type1'],
                "new_store_first_order_discount_value_type": row['business_growth_support__new_store_first_order_discount_value_type'],
                "refurbish_store": row['business_growth_support__refurbish_store_value'],
                "refurbish_store_type": row['business_growth_support__refurbish_store_type'],
                "refurbish_store_value_type": row['business_growth_support__refurbish_store_value_type'],
                "anniversary_sales_allowance": row['business_growth_support__anniversary_sales_allowance_value'],
                "anniversary_sales_allowance_type": row['business_growth_support__anniversary_sales_allowance_type'],
                "anniversary_sales_allowance_value_type": row['business_growth_support__anniversary_sales_allowance_value_type'],
                "anniversary_orders_rebate": row['business_growth_support__anniversary_orders_rebate_value'],
                "anniversary_orders_rebate_type": row['business_growth_support__anniversary_orders_rebate_type'],
                "anniversary_orders_rebate_value_type": row['business_growth_support__anniversary_orders_rebate_value_type'],
                #Promotion Support
                "middle_year_big_sales": row['promotion_support__middle_year_big_sales_value'],
                "middle_year_big_sales_type": row['promotion_support__middle_year_big_sales_type'],
                "middle_year_big_sales_remark": row['promotion_support__middle_year_big_sales_value_type'],
                "top_brand": row['promotion_support__top_brand_value'],
                "top_brand_type": row['promotion_support__top_brand_type'],
                "top_brand_remark": row['promotion_support__top_brand_value_type'],
                "anniversary": row['promotion_support__anniversary_value'],
                "anniversary_type": row['promotion_support__anniversary_type'],
                "anniversary_remark": row['promotion_support__anniversary_value_type'],
                "gawai_sales": row['promotion_support__gawai_sales_value'],
                "gawai_sales_type": row['promotion_support__gawai_sales_type'],
                "gawai_sales_remark": row['promotion_support__gawai_sales_value_type'],
                "anniversary_sales": row['promotion_support__anniversary_sales_value'],
                "anniversary_sales_type": row['promotion_support__anniversary_sales_type'],
                "anniversary_sales_remark": row['promotion_support__anniversary_sales_value_type'],
                "chinese_new_year_sales": row['promotion_support__chinese_new_year_sales_value'],
                "chinese_new_year_sales_type": row['promotion_support__chinese_new_year_sales_type'],
                "chinese_new_year_sales_remark": row['promotion_support__chinese_new_year_sales_value_type'],
                "hari_raya_sales": row['promotion_support__hari_raya_sales_value'],
                "hari_raya_sales_type": row['promotion_support__hari_raya_sales_type'],
                "hari_raya_sales_remark": row['promotion_support__hari_raya_sales_value_type'],
                "christmas_sales": row['promotion_support__christmas_sales_value'],
                "christmas_sales_type": row['promotion_support__christmas_sales_type'],
                "christmas_sales_remark": row['promotion_support__christmas_sales_value_type'],
                "promotion_commission": row['promotion_support__promotion_commission_value'],
                "promotion_commission_type": row['promotion_support__promotion_commission_type'],
                "promotion_commission_remark": row['promotion_support__promotion_commission_value_type'],
                #Display Incentive
                #Marketing Support
                "packaging_fee": row['marketing_support__packaging_fee_value'],
                "packaging_fee_type": row['marketing_support__packaging_fee_type'],
                "packaging_fee_remark": row['marketing_support__packaging_fee_value_type'],
                "loyalty_program": row['marketing_support__loyalty_program_value'],
                "loyalty_program_type": row['marketing_support__loyalty_program_type'],
                "loyalty_program_remark": row['marketing_support__loyalty_program_value_type'],
                "anniversary_event": row['marketing_support__anniversary_event_value'],
                "anniversary_event_type": row['marketing_support__anniversary_event_type'],
                "anniversary_event_remark": row['marketing_support__anniversary_event_value_type'],
                "crm_event": row['marketing_support__crm_event_value'],
                "crm_event_type": row['marketing_support__crm_event_type'],
                "crm_event_remark": row['marketing_support__crm_event_value_type'],
                "marketing_event": row['marketing_support__marketing_event_value'],
                "marketing_event_type": row['marketing_support__marketing_event_type'],
                "marketing_event_remark": row['marketing_support__marketing_event_value_type'],
                "concourse_event": row['marketing_support__concourse_event_value'],
                "concourse_event_type": row['marketing_support__concourse_event_type'],
                "concourse_event_remark": row['marketing_support__concourse_event_value_type'],
                #E-Commerce Support
                "e_commerce_sales": row['e_commerce_support__e_commerce_sales_value'],
                "e_commerce_sales_type": row['e_commerce_support__e_commerce_sales_type'],
                "e_commerce_sales_remark": row['e_commerce_support__e_commerce_sales_value_type'],
                "system_setup_n_maintenance": row['e_commerce_support__system_setup_n_maintenance_value'],
                "system_setup_n_maintenance_type": row['e_commerce_support__system_setup_n_maintenance_type'],
                "system_setup_n_maintenance_remark": row['e_commerce_support__system_setup_n_maintenance_value_type'],
                "digital_communication": row['e_commerce_support__digital_communication_value'],
                "digital_communication_type": row['e_commerce_support__digital_communication_type'],
                "digital_communication_remark": row['e_commerce_support__digital_communication_value_type'],
                "social_media_post": row['e_commerce_support__social_media_post_value'],
                "social_media_post_type": row['e_commerce_support__social_media_post_type'],
                "social_media_post_remark": row['e_commerce_support__social_media_post_value_type'],
                "market_place_event": row['e_commerce_support__market_place_event_value'],
                "market_place_event_type": row['e_commerce_support__market_place_event_type'],
                "market_place_event_remark": row['e_commerce_support__market_place_event_value_type']
        } 

        newlist.append(dataset)
        processed_refnos.add(refno)  # Mark this refno as processed


        # Convert lists to tuples to make them hashable for drop_duplicates
        #for item in newlist:
            #for key, value in item.items():
                #if isinstance(value, list):
                    #item[key] = tuple(value)

        df = pd.DataFrame(newlist)

        #Drop duplicate rows based on all columns
        #df = df.drop_duplicates()

        # Convert tuples back to lists, but leave other values unchanged
        #for column in df.columns:
            #if df[column].apply(lambda x: isinstance(x, tuple)).any():
                #df[column] = df[column].apply(lambda x: list(x) if isinstance(x, tuple) else x)
    
    df = format_numeric_columns(df)

    #return Response(newlist, status=status.HTTP_200_OK)
    
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        
        # Get the xlsxwriter workbook and worksheet objects.
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        # Get the dimensions of the dataframe. 
        (max_row, max_col) = df.shape

        # Iterate through each column and set the width.
        for col in range(max_col):
            column_len = df.iloc[:, col].astype(str).map(len).max()
            column_name = df.columns[col]
            max_len = max(column_len, len(column_name)) + 2
            worksheet.set_column(col, col, max_len)

        #WS_EX_TOPMOST = 0x40000
        #windowTitle = "Exporting RIMS TTA List Excel Sheet"
        #message = "Your excel file has been generated. Click ok to download."

        # display a message box; execution will stop here until user acknowledges
        #ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)

        writer.close()
        #writer.save()

        # Set up the Http response.
        filename = title + '.xlsx'
        #filename = 'test' + '.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response
    

#def export_excel_cal_main(request,customer_guid, date_from, date_to):
# @api_view(['GET'])
# def export_excel_cal_main(request,customer_guid, date_from, date_to): 
#     if request.method == 'GET':   
#         result_status = True

#         customer_guid = str('%s'%customer_guid)
#         date_from = str('%s'%date_from)
#         date_to = str('%s'%date_to) 
#         title = 'calmain_'+customer_guid+'_'+date_from+'_'+date_to
        
#         result = TtaListCalMain.objects.filter(customer_guid=customer_guid)
        
#         return Response(result, status=status.HTTP_200_OK)
#         with BytesIO() as b:
#             # Use the StringIO object as the filehandle.  
#             df = pd.DataFrame(result) 

#             writer = pd.ExcelWriter(b, engine='xlsxwriter')
#             df.to_excel(writer, sheet_name='Sheet1', index=False)
#             writer.close()
#             # Set up the Http response.
#             filename = title+'.xlsx'
#             response = HttpResponse(
#                 b.getvalue(),
#                 content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#             )
#             response['Content-Disposition'] = 'attachment; filename=%s' % filename
#             return response


#     # data = {
#     #         "status": True,
#     #         "message": customer_guid,
#     #         "retailer_guid": customer_guid
#     #     } 
#     #return Response(data, status=status.HTTP_200_OK)


#     return Response(result, status=status.HTTP_200_OK)
