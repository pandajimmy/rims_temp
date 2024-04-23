from .models import CustomerUrl
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class CustomerUrlSerializer(serializers.ModelSerializer):
    # value = serializers.SerializerMethodField('get_value')
    # label = serializers.SerializerMethodField('get_label')

    # def get_value(self, obj):
    #     return obj.customer_guid

    # def get_label(self, obj):
    #     return obj.customer_name

 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    class Meta:
        model = CustomerUrl
 #      depth = 1
        fields = '__all__'
        # fields = (
        #     'value',
        #     'label',
        # )

    # def to_representation(self, instance):
    #     ret = super(CustomerUrlSerializer, self).to_representation(instance)
    #     # check the request is list view or detail view
    #     is_list_view = isinstance(self.instance, list)
    #     extra_ret = {'selected': "false"} #if is_list_view else {'key': 'single value'}
    #     ret.update(extra_ret)
    #     return ret