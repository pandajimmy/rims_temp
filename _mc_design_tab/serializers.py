from .models import DesignTab
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
#from _mc_design_row.serializers import DesignRowSerializer
from _mc_design_dynamic.serializers import DesignDynamicSerializer

class DesignTabSerializer(serializers.ModelSerializer):

      child_design_tab = DesignDynamicSerializer(many=True, read_only=True)

      class Meta:
            model = DesignTab
            #      depth = 1
            #fields = '__all__'
            fields = ( 
                     'template_guid',
                     'tab_guid',
                     'key_description',
                     'description',
                     'sequence',
                     'child_design_tab',
              )

      def to_representation(self, instance):
        ret = super(DesignTabSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret