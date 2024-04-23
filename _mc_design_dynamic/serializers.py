from .models import DesignDynamic
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
#from _mc_design_tab.serializers import DesignTabSerializer


class DesignDynamicSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
     # child_design_tab = DesignTabSerializer(many=True, read_only=True)
      class Meta:
            model = DesignDynamic
            #      depth = 1
            fields = '__all__'

      def to_representation(self, instance):
        ret = super(DesignDynamicSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret