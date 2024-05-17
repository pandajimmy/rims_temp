from .models import TtaListECommerceSupport
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListECommerceSupportSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListECommerceSupport
 #      depth = 1
        fields = '__all__'