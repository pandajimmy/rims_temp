from .models import TtaListBusinessGrowthSupport
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListBusinessGrowthSupportSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListBusinessGrowthSupport
 #      depth = 1
        fields = '__all__'