from .models import TtaListDisplayIncentive
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListDisplayIncentiveSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListDisplayIncentive
 #      depth = 1
        fields = '__all__'