from .models import TtaListForm
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListFormSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
       class Meta:
              model = TtaListForm
       #      depth = 1
              fields = '__all__'

       # def to_representation(self, obj):
       #  if isinstance(obj, dict): # get methods
       #      return obj
       #  else:
       #      return super(TtaListFormSerializer, self).to_representation(obj)

       # def create(self, validated_data):
       #        question = TtaListForm.objects.create(**validated_data)
       #        return question
       