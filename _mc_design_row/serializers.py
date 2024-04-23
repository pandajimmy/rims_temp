from .models import DesignRow
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_design_column.serializers import DesignColumnSerializer

class DesignRowSerializer(serializers.ModelSerializer):
       columns = DesignColumnSerializer(many=True, read_only=True)
       class Meta:
              model = DesignRow
       #      depth = 1
              # fields = '__all__'
              fields = (
                     # 'column_guid',
                     # 'created_at',
                     # 'created_by',
                     # 'updated_at',
                     # 'updated_by'
                     # 'row_guid',
                     'seq',
                     'size',
                     'columns',
              )