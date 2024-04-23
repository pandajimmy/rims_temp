from .models import MainFilter
from rest_framework import serializers
from _mc_main_filter_child.serializers import MainFilterChildSerializer


class MainFilterSerializer(serializers.ModelSerializer):
       child_filter_type = MainFilterChildSerializer(many=True, read_only=True)
       class Meta:
              model = MainFilter
       #      depth = 1
              # fields = '__all__'
              fields = (
                            'main_filter_guid',
                            'code',
                            'description',
                            'child_filter_type',
                     )