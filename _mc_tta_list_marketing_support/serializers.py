from .models import TtaListMarketingSupport
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListMarketingSupportSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListMarketingSupport
 #      depth = 1
        fields = '__all__'