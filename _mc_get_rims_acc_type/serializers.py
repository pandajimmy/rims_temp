from .models import RimsAccType
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsAccTypeSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsAccType
 #      depth = 1
        fields = '__all__'