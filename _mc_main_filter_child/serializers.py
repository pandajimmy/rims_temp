from .models import MainFilterChild
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class MainFilterChildSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = MainFilterChild
 #      depth = 1
        # fields = '__all__'
        fields = (
                     'cols_size',
                     'sm_size',
                     'md_size',
                     'lg_size',
                     'xl_size',
                     'placeholder',
                     'id',
                     'name',
                     'parameter',
                     'seq',
                     'option_type',
                     'is_active'
                     )