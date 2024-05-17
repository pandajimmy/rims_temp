from .models import TtaListPaymentNDiscount
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListPaymentNDiscountSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListPaymentNDiscount
 #      depth = 1
        fields = '__all__'