from .models import RimsDivDeptSdC
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsDivDeptSdCSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsDivDeptSdC
 #      depth = 1
        fields = '__all__'