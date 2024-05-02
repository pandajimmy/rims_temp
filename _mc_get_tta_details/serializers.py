from .models import TtaListDetails
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_get_tta_details_child.serializers import TtaListFormSerializer

class TtaListDetailsSerializer(serializers.ModelSerializer):
       dynamic_field = TtaListFormSerializer(many=True, read_only=True)
       class Meta:
              model = TtaListDetails
       #      depth = 1
              fields = '__all__'