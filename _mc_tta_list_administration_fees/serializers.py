from .models import TtaListAdministrationFees
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListAdministrationFeesSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListAdministrationFees
 #      depth = 1
        fields = '__all__'