from .models import TtaInvmain
from rest_framework import serializers
from django.core.exceptions import ValidationError
#from subdept.serializers import subdeptserializer

from _ts_tta_invchild.serializers import TtaInvchildSerializer

class TtaInvmainSerializer(serializers.ModelSerializer):
#       subdept_key = SubdeptSerializer(many=True, read_only=True)
    invchild_key = TtaInvchildSerializer(many=True, read_only=True)


    class Meta:
        model = TtaInvmain
        #depth = 1
        fields = '__all__'
        