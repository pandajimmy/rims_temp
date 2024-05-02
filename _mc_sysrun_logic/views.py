from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import uuid
from _mc_get_customer_url.models import CustomerUrl
from _mc_get_acc_internal.models import AccInternal
from _ml_rims_customer_data.models import RimsCustomerData
from _ts_tta_list.models import TtaList_ts
from _lib import panda
from django.db import connection
from rest_framework.decorators import api_view


def generate_uuid():
    return uuid.uuid4().hex.upper()
# Create your views here.
def index(request):
    return HttpResponse("This is the index page.")


def try_query(request, datefrom, dateto):
    with connection.cursor() as cursor:
        cursor.execute("SELECT acc_user_id FROM acc_user")
        
        row = cursor.fetchall()

    return row

@api_view(['GET'])
def info_rims_summarized(request, datefrom, dateto):

    querystr = """
    SELECT loc_group,CODE AS sup_code,name_reg AS sup_name,Brand,brand_desc,SUM(gr_amt) AS gr_amt,SUM(gr_surchg) AS gr_surchg,
SUM(debitamt) AS debitamt,SUM(debit_surchg) AS debit_surchg,SUM(creditamt) AS creditamt,SUM(credit_surchg) AS credit_surchg,
SUM(PDNamt) AS PDNamt,SUM(PCNamt) AS PCNamt
FROM 
(
SELECT loc_group, a.Code,c.name_reg,b.Brand,br.`Description` AS brand_desc,
ROUND(SUM(subtotal1),2) AS gr_amt,ROUND(IF(d.refno IS NULL,0,SUM(value_calculated)),2) AS gr_surchg,
0 AS debitamt,0 AS debit_surchg,0 AS creditamt,0 AS credit_surchg,0 AS PDNamt,0 AS PCNamt
FROM backend.grmain a 
INNER JOIN backend.grchild b
ON a.RefNo=b.refno
LEFT JOIN backend.brand br
ON b.Brand=br.Code
INNER JOIN backend.supcus c
ON a.Code=c.Code
LEFT JOIN backend.trans_surcharge_discount d
ON a.RefNo=d.refno AND trans_type='GRN' AND d.dn=0
WHERE a.`BillStatus`=1 AND a.`ibt`=0  AND in_kind=0 
AND grdate BETWEEN CONVERT(%s %datefrom USING  latin1) AND CONVERT(%s %dateto USING  latin1)
 
GROUP BY a.Code,b.Brand, loc_group

UNION ALL

SELECT locgroup,a.Code,c.name_reg,b.Brand,br.`Description` AS brand_desc,0 AS gr_amt,0 AS gr_surchg,
ROUND(SUM(subtotal1),2) AS debitamt,ROUND(IF(d.refno IS NULL,0,SUM(value_calculated)),2) AS debit_surchg,
0 AS creditamt,0 AS credit_surchg,0 AS PDNamt,0 AS PCNamt
FROM backend.dbnotemain a 
INNER JOIN backend.dbnotechild b
ON a.RefNo=b.refno
LEFT JOIN backend.brand br
ON b.Brand=br.Code
INNER JOIN backend.supcus c
ON a.Code=c.Code
LEFT JOIN backend.trans_surcharge_discount d
ON a.RefNo=d.refno AND trans_type='GRDN' AND d.dn=0
WHERE a.sctype='S' AND a.`BillStatus`=1 AND a.`ibt`=0
AND docdate BETWEEN CONVERT(%s %datefrom USING  latin1) AND CONVERT(%s %dateto USING  latin1)

GROUP BY a.Code,b.Brand, locgroup

UNION ALL

SELECT locgroup,a.Code,c.name_reg,b.Brand,br.`Description` AS brand_desc,0 AS gr_amt,0 AS gr_surchg,0 AS debitamt,0 AS debit_surchg,
ROUND(SUM(subtotal1),2) AS creditamt,ROUND(IF(d.refno IS NULL,0,SUM(value_calculated)),2) AS credit_surchg,
0 AS PDNamt,0 AS PCNamt
FROM backend.cnnotemain a 
INNER JOIN backend.cnnotechild b
ON a.RefNo=b.refno
LEFT JOIN backend.brand br
ON b.Brand=br.Code
INNER JOIN backend.supcus c
ON a.Code=c.Code
LEFT JOIN backend.trans_surcharge_discount d
ON a.RefNo=d.refno AND trans_type='CN' AND d.dn=0
WHERE a.sctype='S' AND a.`BillStatus`=1 AND a.`ibt`=0
AND docdate BETWEEN CONVERT(%s %datefrom USING  latin1) AND CONVERT(%s %dateto USING  latin1)

GROUP BY a.Code,b.Brand, locgroup

UNION ALL

SELECT loc_group,a.Code,c.name_reg,b.Brand,br.`Description` AS brand_desc,0 AS gr_amt,0 AS gr_surchg,0 AS debitamt,0 AS debit_surchg,
0 AS creditamt,0 AS credit_surchg,
ROUND(SUM(IF(trans_type='PDNAMT',amount,0)),2) AS PDNamt,ROUND(SUM(IF(trans_type='PCNAMT',amount,0)),2) AS PCNamt
FROM backend.cndn_amt a 
INNER JOIN backend.cndn_amt_c b
ON a.cndn_guid=b.cndn_guid
LEFT JOIN backend.brand br
ON b.Brand=br.Code
INNER JOIN backend.supcus c
ON a.Code=c.Code
WHERE a.`posted`=1 AND a.`ibt`=0 AND trans_type IN ('PDNAMT','PCNAMT') AND trans_type_acc='COGS'
AND docdate BETWEEN CONVERT(%s %datefrom USING  latin1) AND CONVERT(%s %dateto USING  latin1)

GROUP BY a.Code,b.Brand,loc_group

)a

GROUP BY CODE,Brand, loc_group
ORDER BY CODE,Brand
    """

    result = panda.raw_query(querystr, [search_refno])
    result = {"Grmain_dncn": result}

    return Response(result, status=status.HTTP_200_OK)

def first_calculation(request, customer_guid):
    if len(customer_guid) == 32: #make sure guid is 32 characters
        get_URL = CustomerUrl.objects.filter(customer_guid='%s' %customer_guid).first()
            #print(get_URL)
        if get_URL != None: #make sure guid is valid
            return HttpResponse("Exist")
        else:
            return HttpResponse("Customer Guid not found")
    
    else:
        return HttpResponse("Invalid Guid")


