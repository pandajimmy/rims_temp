from .models import TtaListPromotionSupport
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListPromotionSupportSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListPromotionSupport
 #      depth = 1
        fields = '__all__'