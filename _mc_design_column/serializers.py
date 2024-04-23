from .models import DesignColumn
from rest_framework import serializers
from _mc_design_component.serializers import DesignComponentSerializer


class DesignColumnSerializer(serializers.ModelSerializer):
       components = DesignComponentSerializer(many=True, read_only=True)
       class Meta:
              model = DesignColumn
       #      depth = 1
              # fields = '__all__'
              fields = (
                     # 'column_guid',
                     # 'created_at',
                     # 'created_by',
                     # 'updated_at',
                     # 'updated_by',
                     # 'row_guid',
                     'seq',
                     'cols_size',
                     'sm_size',
                     'md_size',
                     'lg_size',
                     'xl_size',
                     'components',
              )