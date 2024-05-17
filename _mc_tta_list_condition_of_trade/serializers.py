from .models import TtaListConditionOfTrade
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListConditionOfTradeSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListConditionOfTrade
 #      depth = 1
        fields = '__all__'