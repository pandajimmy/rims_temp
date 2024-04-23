from django.http import JsonResponse
from rest_framework.decorators import api_view
#from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

from _lib import rims_data_functions
from decimal import Decimal

from .rims_data_functions import rebate
from .rims_data_functions import gr_sum

import sys

@api_view(['GET'])
def calculation(request):
    
    if request.method == 'GET':

        data = {
            "customer_guid":"D361F8521E1211EAAD7CC8CBB8CC0C93", # allow only one,example EVERRISE,TF,MIDAS,ETC
            "type":"gr_gross_sum", #gr_gross_sum, gr_net_sum
            "startDate":"2022-08-01",
            "endDate": "2022-08-31",
            "outlet": ['4M', 'BDC', 'BK', 'BMM', 'C1', 'DL', 'ESK', 'FC', 'GHM', 'HQ', 'KR', 'KS', 'MET', 'MJ', 'MSB', 'PDN', 'PEN', 'PMR', 'VIV'],
            "brand": [],
            "supcode":[
                "H0124-G"
            ],
            "bf_amount":Decimal(0.5),
            "rebate_method":[
                {
                    "range":5000,
                    "type":"%",
                    "value":0.5
                },
                {
                    "range":10000,
                    "type":"%",
                    "value":3
                },
                {
                    "range":99999999,
                    "type":"%",
                    "value":5
                }
            ]
        }

    #     data = {
    #     "customer_guid": "D361F8521E1211EAAD7CC8CBB8CC0C93",
    #     "type": "gr_net_sum",
    #     "startDate": "2022-08-01",
    #     "endDate": "2022-08-31",
    #     "outlet": ['4M', 'BDC', 'BK', 'BMM', 'C1', 'DL', 'ESK', 'FC', 'GHM', 'HQ', 'KR', 'KS', 'MET', 'MJ', 'MSB', 'PDN', 'PEN', 'PMR', 'VIV'],
    #     "brand": [],
    #     "supcode": [
    #         "H0124"
    #     ],
    #     "bf_amount": Decimal(0.00),
    #     "rebate_method": [
    #         {
    #             "range": Decimal(5000000.00),
    #             "type": "%",
    #             "value": Decimal(0.5)
    #         },
    #         {
    #             "range": Decimal(7000000.00),
    #             "type": "%",
    #             "value": Decimal(1.0)
    #         },
    #         {
    #             "range": Decimal(9500000.00),
    #             "type": "%",
    #             "value": Decimal(1.50)
    #         }
    #     ]
    # }
        # to cal rebate
        #result = rims_data_functions.rebate(data) 
        result = rims_data_functions.gr_query_sum_group_outlet_div(data)
        
        #to cal gr_sum
        #result = gr_sum(data)
        print(result)
        #sys.exit(1) 
    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_cal(request):
    print("start api")
    
    return Response('', status=status.HTTP_200_OK)
        