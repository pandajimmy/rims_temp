from .models import TtaListStockNDeliveries
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListStockNDeliveriesSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListStockNDeliveries
 #      depth = 1
        fields = '__all__'