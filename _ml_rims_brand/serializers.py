from .models import RimsBrand
from rest_framework import serializers


class RimsBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RimsBrand
 #      depth = 1
        fields = '__all__'