from .models import TtaListTradingGroup
from _ml_rims_div_dept_sd_c.serializers import RimsDivDeptSdCSerializer
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListTradingGroupSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

    group_details = RimsDivDeptSdCSerializer(read_only=True, source='trans_guid')    

    class Meta:
        model = TtaListTradingGroup
 #      depth = 1
        fields = '__all__'
        read_only_fields = ['list_group_guid']

