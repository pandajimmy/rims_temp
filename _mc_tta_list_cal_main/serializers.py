from .models import TtaListCalMain
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListCalMainSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListCalMain
 #      depth = 1
        fields = '__all__'