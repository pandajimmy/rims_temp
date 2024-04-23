from .models import AccInternal
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class AccInternalSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AccInternal
 #      depth = 1
        fields = '__all__'
       
    # def to_representation(self, instance):
    #     ret = super(AccInternalSerializer, self).to_representation(instance)
    #     # check the request is list view or detail view
    #     is_list_view = isinstance(self.instance, list)
    #     extra_ret = {'selected': "false"} #if is_list_view else {'key': 'single value'}
    #     ret.update(extra_ret)
    #     return ret