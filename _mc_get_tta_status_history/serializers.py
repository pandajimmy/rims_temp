from .models import TtaList
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaList
 #      depth = 1
        fields = '__all__'