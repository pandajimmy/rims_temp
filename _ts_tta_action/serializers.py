
from rest_framework import serializers
from django.core.exceptions import ValidationError

#from _ts_tta_invmain.serializers import TtaInvmainSerializer


class update_ttachild_serializers(serializers.Serializer):  
    customer_guid = serializers.CharField(max_length=32)
    line = serializers.IntegerField(max_value=None, min_value=1)
    pricetype = serializers.DecimalField(max_digits=14, decimal_places=2)
    itemcode = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50)
    qty = serializers.DecimalField(max_digits=14, decimal_places=2)
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=2)
    disc1type = serializers.ChoiceField(choices=('$','%',))
    disc1value =serializers.DecimalField(max_digits=14, decimal_places=2)
    disc2type =serializers.CharField(max_length=20)
    disc2value =serializers.DecimalField(max_digits=14, decimal_places=2)
    totalprice =serializers.DecimalField(max_digits=14, decimal_places=2)
    gst_tax_code =serializers.CharField(max_length=10)
    gst_tax_rate =serializers.DecimalField(max_digits=14, decimal_places=2)
    gst_tax_amount =serializers.DecimalField(max_digits=14, decimal_places=2)
    total_incl_tax =serializers.DecimalField(max_digits=14, decimal_places=2)