from .models import TtaCndnAmtC
from rest_framework import serializers
from django.core.exceptions import ValidationError 

#from _ts_tta_invchild.serializers import TtaInvchildSerializer

class TtaCndnAmtCSerializer(serializers.ModelSerializer):
#       subdept_key = SubdeptSerializer(many=True, read_only=True)
    #invchild_key = TtaInvchildSerializer(many=True, read_only=True)


    class Meta:
        model = TtaCndnAmtC
        #depth = 1
        fields = '__all__'
        