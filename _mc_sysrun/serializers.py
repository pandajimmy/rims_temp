from .models import Sysrun
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class SysrunSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = Sysrun
 #      depth = 1
        fields = '__all__'