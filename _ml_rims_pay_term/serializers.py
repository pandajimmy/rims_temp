from .models import RimsPayTerm
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsPayTermSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsPayTerm
 #      depth = 1
        fields = '__all__'