from .models import TtaListOutlet
from _ml_rims_cp_set_branch.serializers import RimsCpSetBranchSerializer
from rest_framework import serializers
#from subdept.serializers import subdeptserializer

class TtaListOutletSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

    branch = RimsCpSetBranchSerializer(read_only=True, source='branch_guid') 

    class Meta:
        model = TtaListOutlet
 #      depth = 1
        fields = '__all__'