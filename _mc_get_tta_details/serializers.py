from .models import TtaList
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_get_tta_details_child.serializers import TtaListFormSerializer

class TtaListSerializer(serializers.ModelSerializer):
       dynamic_field = TtaListFormSerializer(many=True, read_only=True)
       class Meta:
              model = TtaList
       #      depth = 1
              fields = '__all__'