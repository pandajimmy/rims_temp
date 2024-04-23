from .models import TtaList
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class TtaListSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
      class Meta:
            model = TtaList
            #      depth = 1
            fields = '__all__'

      def to_representation(self, instance):
        ret = super(TtaListSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret
      
      def view(request):
            print('123')
            return Response({"message": "Hello for today! See you tomorrow!"})

      