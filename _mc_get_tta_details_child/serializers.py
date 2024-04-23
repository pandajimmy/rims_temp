from .models import TtaListForm
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListFormSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = TtaListForm
 #      depth = 1
        fields = '__all__'