from .models import RimsCpSetBranch
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsCpSetBranchSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsCpSetBranch
 #      depth = 1
        fields = '__all__'