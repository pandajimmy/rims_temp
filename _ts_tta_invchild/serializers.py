from .models import TtaInvchild
from rest_framework import serializers
from django.core.exceptions import ValidationError

#from _ts_tta_invmain.serializers import TtaInvmainSerializer


class TtaInvchildSerializer(serializers.ModelSerializer):
    #invchild_key = TtaInvmainSerializer(many=True, read_only=True)

    class Meta:
        model = TtaInvchild
        #depth = 1
        fields = '__all__'
        