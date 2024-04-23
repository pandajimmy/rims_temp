from .models import SetUser
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class SetUserSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = SetUser
 #      depth = 1
        fields = '__all__'