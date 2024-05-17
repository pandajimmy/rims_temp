from .models import TtaListTradingBrand
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListTradingBrandSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListTradingBrand
 #      depth = 1
        fields = '__all__'
        read_only_fields = ['list_brand_guid', 'refno', 'code']
