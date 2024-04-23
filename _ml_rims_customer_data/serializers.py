from .models import RimsCustomerData
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsCustomerDataSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsCustomerData
 #      depth = 1
        fields = '__all__'