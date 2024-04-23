from .models import TtaListStatus
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListStatusSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListStatus
 #      depth = 1
        fields = '__all__'