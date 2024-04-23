from .models import AccUser
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class AccUserSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = AccUser
 #      depth = 1
        fields = '__all__'