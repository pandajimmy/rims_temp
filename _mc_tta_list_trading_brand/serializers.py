from .models import TtaListTradingBrand
from _ml_rims_brand.serializers import RimsBrandSerializer
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListTradingBrandSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

    brand = RimsBrandSerializer(read_only=True, source='brand_guid')    

    class Meta:
        model = TtaListTradingBrand
 #      depth = 1
        fields = '__all__'
        read_only_fields = ['list_brand_guid']

