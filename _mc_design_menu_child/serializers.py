from .models import DesignMenuChild
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class DesignMenuChildSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = DesignMenuChild
 #      depth = 1
        fields = '__all__'