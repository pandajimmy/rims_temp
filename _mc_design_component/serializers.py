from .models import DesignComponent
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class DesignComponentSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = DesignComponent
 #      depth = 1
        # fields = '__all__'
        fields = (
            # 'column_guid',
            # 'component_guid',
            # 'created_at',
            # 'created_by',
            # 'updated_at',
            # 'updated_by',
            'seq',
            'cols_size',
            'sm_size',
            'md_size',
            'lg_size',
            'xl_size',
            'offset_cols_size',
            'offset_sm_size',
            'offset_md_size',
            'offset_lg_size',
            'offset_xl_size',
            'group',
            'input_type',
            'rows',
            'id',
            'name',
            'placeholder',
            'text',
            'type',
            'option_url',
            'left_option_url',
            'left_label',
            'left_option_id',
            'dynamic'
        )