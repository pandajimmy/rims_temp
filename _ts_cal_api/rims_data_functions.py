
from email.policy import default
from random import choices
from rest_framework import serializers
from _mc_tta_list_cal_main.models import TtaListCalMain 
from django.db.models import Sum,F

def gr_net_sum_cal():
    return ((F('gr_amt')-F('gr_surchg')) - (F('debitamt')-F('debit_surchg')) + (F('creditamt')-F('credit_surchg')))

def gr_gross_sum_cal():
    return (F('gr_amt')-F('gr_surchg'))

class rebateSerializer(serializers.Serializer):
    range = serializers.FloatField(max_value=None, min_value=0)
    type = serializers.ChoiceField(choices=('$','%',))
    value = serializers.FloatField(max_value=None, min_value=0)

class fgr_sumSerializer(serializers.Serializer):
    gr_sum_type = ("gr_gross_sum","gr_net_sum",)

    customer_guid = serializers.CharField(max_length=32)
    type =  serializers.ChoiceField(choices=gr_sum_type)
    startDate = serializers.CharField(max_length=10)
    endDate = serializers.CharField(max_length=10)
    outlet = serializers.ListField(child = serializers.CharField(max_length=12))
    supcode = serializers.ListField(child = serializers.CharField(max_length=12))
    brand = serializers.ListField(child = serializers.CharField(max_length=12))
    bf_amount =serializers.FloatField(max_value=None, min_value=0)
    rebate_method = serializers.ListField(child = rebateSerializer())

def filterdata(param):
    if len(param["brand"]) == 0:
        if len(param["supcode"]) == 0 and len(param["outlet"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]]}
        elif len(param["outlet"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]], "sup_code__in":param["supcode"]}
        elif len(param["supcode"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]],"outlet__in":param["outlet"]}
        else:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]],"outlet__in":param["outlet"], "sup_code__in":param["supcode"]}
    else:
        if len(param["supcode"]) == 0 and len(param["outlet"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]], "brand__in":param["brand"]}
        elif len(param["outlet"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]], "sup_code__in":param["supcode"], "brand__in":param["brand"]}
        elif len(param["supcode"]) == 0:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]],"outlet__in":param["outlet"], "brand__in":param["brand"]}
        else:
            filter = {"customer_guid": param["customer_guid"],"docdate__range" : [param["startDate"], param["endDate"]],"outlet__in":param["outlet"], "sup_code__in":param["supcode"], "brand__in":param["brand"]}
    return filter
    
def gr_query_sum(param): 
    if param['type'] == 'gr_net_sum':
        gr_formula = ((F('gr_amt')-F('gr_surchg')) - (F('debitamt')-F('debit_surchg')) + (F('creditamt')-F('credit_surchg')))
    else:
        gr_formula =  (F('gr_amt')-F('gr_surchg'))

    filtered_data = TtaListCalMain.objects \
                .filter(**filterdata(param)) \
                .annotate(total=gr_formula) \
                .aggregate(Sum("total"))

    return filtered_data["total__sum"]

def gr_sum(param):
    serializer =fgr_sumSerializer(data=param)
    if serializer.is_valid()==False:
        return {"status":False, "message":serializer.errors}

    gr_sum = gr_query_sum(param)

    if gr_sum == None:
        gr_sum = 0
    return {"status":True, "value":gr_sum}

def calRebate(calType, calValue, calAmount):
    if calType == '$' or calType == 'RM':
        return calValue
    if calType == '%':
        return round((calValue / 100) * float(calAmount), 4)

def rebate(param): 
    json = []
    purchase = gr_sum(param)
    if purchase["status"] == False:
        return purchase
    pur_amount = purchase["value"]
    bf_amount = param["bf_amount"] 
    accum_pur_amount = bf_amount + pur_amount
    #accum_pur_amount = 100
    for rebate_method in param['rebate_method']:
        if bf_amount<= rebate_method["range"]:
            method_amount_bal = rebate_method["range"]-bf_amount
            if accum_pur_amount-bf_amount<=method_amount_bal:
                actRebateAmt = accum_pur_amount-bf_amount
            else:
                actRebateAmt = method_amount_bal
            bf_amount = bf_amount + actRebateAmt
            jsonChild = rebate_method
            jsonChild["tierPurchaseAmt"] = actRebateAmt
            jsonChild["rebateValue"] = calRebate(rebate_method['type'], rebate_method['value'], actRebateAmt)
            json.append(jsonChild)
        else:
            jsonChild = rebate_method
            jsonChild["tierPurchaseAmt"] = 0  
            jsonChild["rebateValue"] = 0
            json.append(jsonChild)

    purchase['rebate'] = json

    return purchase
