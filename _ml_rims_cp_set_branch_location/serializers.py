from .models import RimsCpSetBranchLocation
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsCpSetBranchLocationSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsCpSetBranchLocation
 #      depth = 1
        fields = '__all__'