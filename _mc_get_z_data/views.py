from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import requests
import json
import uuid
from _mc_get_customer_url.models import CustomerUrl
from _mc_get_acc_internal.models import AccInternal
from _ml_rims_customer_data.models import RimsCustomerData
from _ts_tta_list.models import TtaList_ts
from _lib import panda
from django.db import connection


def generate_uuid():
    return uuid.uuid4().hex.upper()
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, customer_guid):
    if len(customer_guid) == 0:
        return HttpResponse("Variable cannot be empty.")
    # elif len(customer_guid) != 32:
    #     return HttpResponse("Guid is not valid %s")
    else:
        return HttpResponse("Valid guid %s." %customer_guid)

def results(request, customer_guid):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % customer_guid)

def vote(request, customer_guid):
    return HttpResponse("You're voting on question %s." % customer_guid)

def home(request, customer_guid):
    #response = requests.get('https://api.covid19api.com/summary').json() 
    response = requests.get('https://api.covid19api.com/summary') 
    content = json.loads(response.content)
    # change the JSON string into a JSON object
    jsonObject = json.loads(response.content)

    # print the keys and values
    for key in jsonObject:
        value = jsonObject[key]
        HttpResponse("The key and value are ({}) = ({})".format(key, value))
    
    pass 
    # key = content['Global']['NewDeaths']  
    # return HttpResponse(key)

def pnl(request, customer_guid,list_guid, date_to, date_from, date):
    for key in jsonObject:
        value = jsonObject[key]
        HttpResponse("The key and value are ({}) = ({})".format(key, value))
    
    
    # row = cursor.fetchall()
    # return HttpResponse(row)

    #check customer_guid validity
    if CustomerUrl.objects.filter(customer_guid='%s' %customer_guid):
        #print("There is at least one Entry with the customer_guid")
        get_URL = CustomerUrl.objects.filter(customer_guid='%s' %customer_guid).first()
        get_InternalURL = AccInternal.objects.filter(internal_name='internal_log').first()

        #make sure list_guid exist
        if TtaList_ts.objects.filter(list_guid='%s' %list_guid): 
            get_TTAList_data = TtaList_ts.objects.filter(list_guid='%s' %list_guid).first()
            supplier_guid = get_TTAList_data.supplier_guid
            supplier_code = get_TTAList_data.supplier_code
            tta_period_from = get_TTAList_data.tta_period_from
            tta_period_to = get_TTAList_data.tta_period_to


        else:
            return HttpResponse('List ID does not exist')

        #get pnl data from source 
        #customer_guid 8D5B38E931FA11E79E7E33210BD612D3
        #list_guid  9C0025574BFE48A68946CD7A4BDF1E97
        response = requests.post(get_URL.customer_url+'pnlcategory/', json={'date_from':'%s' %date_from, 'date_to':'%s' %date_to})
        #fail 
        if response.status_code != 200 : 
            json_log = {
                "url" : get_URL.customer_url+'pnlcategory/',
                "post_data" : {'date_from':'%s' %date_from, 'date_to':'%s' %date_to}
            }

            json_data = {
                "log_guid": generate_uuid(), 
                "customer_guid": '%s' %customer_guid,
                "log_module": "Get:PnL_category",
                "log_ref": '%s' %list_guid,
                "created_by": response.status_code,
                "log_json": json_log
            } 
            response_log = requests.post(get_InternalURL.internal_url+'mc_tta_logs/mc_TtaLogs/', json=json_data)  
            return HttpResponse(response.status_code)
        #success
        else:                                                                           
            json_response = response.json() 
            #insert into log table
            json_data = {
                "log_guid": generate_uuid(), 
                "customer_guid": '%s' %customer_guid,
                "list_guid": '%s' %list_guid,
                "log_module": "Get:PnL_category",
                "log_ref": "mc_get_z_data/pnl", 
                "created_by": "task_agent",
                "log_json": json_response
            }

            response_log = requests.post(get_InternalURL.internal_url+'mc_tta_logs/mc_TtaLogs/', json=json_data)
            #get respond data
            json_response1 = response.json()

            #filter out json data only subject to tta list requirement
            #check outlet involved
            #check subdept dept
            #remaining data put in data_json
            #flag tta_list to ready for calculation

            entry_data = {
                "data_guid": generate_uuid(), 
                "customer_guid": '%s' %customer_guid,
                "list_guid": '%s' %list_guid,
                "date_from": '%s' %date_from,
                "date_to": '%s' %date_to,
                "module_type": "Get:PnL_category",
                #"period_code": '%s' %date_from[0:7],
                "created_by": "task_agent",
                "created_at": panda.panda_today(),
                "data_json": json_response
            }

            response_entry = requests.post(get_InternalURL.internal_url+'ml_rims_customer_data/ml_RimsCustomerData/', json=entry_data)
            if response_entry.status_code != 201:
                json_log = {
                    "url" : get_InternalURL.internal_url+'ml_rims_customer_data/ml_RimsCustomerData/',
                    "post_data" : entry_data
                }

                error_log = {
                    "log_guid": generate_uuid(), 
                    "customer_guid": '%s' %customer_guid,
                    "log_module": "RCD:PnL_category",
                    "log_ref": '%s' %list_guid,
                    "created_by": response_entry.status_code,
                    "log_json": json_log,
                    "remark": response_entry.json()
                } 
                response_log = requests.post(get_InternalURL.internal_url+'mc_tta_logs/mc_TtaLogs/', json=error_log)  
                #return HttpResponse("Insert into RCD:"+str(response_entry.status_code))
                return HttpResponse(response_entry.json())
            else:

                return HttpResponse(json_response)

    else:
        return HttpResponse("Invalid Id")

def calculate_pnl_category(request, customer_guid, period_code):

    if RimsCustomerData.objects.filter(customer_guid='%s' %customer_guid):
        check_period = RimsCustomerData.objects.filter(customer_guid='%s' %customer_guid, period_code='%s' %period_code)
        if check_period.exists():
            get_data = check_period.last()
            if get_data.data_json is None :
                return HttpResponse("No json string for this period : '%s'" %period_code)
            else:
                #correct data to start calculation
                #return HttpResponse(get_data)
                access = get_data.data_json  
                
                # Filter python objects with list comprehensions 
                output_dict = [x for x in access if x['code'] == 'WK']

                # Transform python object back into json
                output_json = json.dumps(output_dict)

                # Show json in http
                #return HttpResponse(output_json) 
                #return HttpResponse(access)
                return HttpResponse(output_json)
                # access value
                # for check in output_json:
                #     print(check[0])
                    
                #aaa = serializers.serialize('json', access, fields=('period_code'))
                #return HttpResponse(aaa, content_type='application/json')
                
                
        else:
            return HttpResponse("No data for this period : '%s'" %period_code)
    else:
        return HttpResponse("Invalid pnl_category Id") 





