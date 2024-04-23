from .models import FormOptionValue
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class FormOptionValueSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = FormOptionValue
 #      depth = 1
        # fields = '__all__'
        fields = (
            # 'created_at',
            # 'created_by',
            # 'updated_at',
            # 'updated_by',
            # 'option_child_guid',
            # 'option_default',
            # 'option_description',
            # 'option_guid',
            # 'option_type',
            # 'option_value',
            # 'option_seq',
            'label',
            'value',
            'selected'
        )