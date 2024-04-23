from .models import RimsBanner
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class RimsBannerSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = RimsBanner
 #      depth = 1
        fields = '__all__'