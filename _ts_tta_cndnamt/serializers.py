from .models import TtaCndnAmt
from rest_framework import serializers
from django.core.exceptions import ValidationError 

from _ts_tta_cndnamt_child.serializers import TtaCndnAmtCSerializer

class TtaCndnAmtSerializer(serializers.ModelSerializer):
#       subdept_key = SubdeptSerializer(many=True, read_only=True)
    cndn_guid_key = TtaCndnAmtCSerializer(many=True, read_only=True)


    class Meta:
        model = TtaCndnAmt
        #depth = 1
        fields = '__all__'
