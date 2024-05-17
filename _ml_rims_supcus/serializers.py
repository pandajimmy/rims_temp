from .models import RimsSupcus
from rest_framework import serializers
from django.core.exceptions import ValidationError
#from subdept.serializers import subdeptserializer


class RimsSupcusSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
    value = serializers.SerializerMethodField('get_value')
    label = serializers.SerializerMethodField('get_label')
    #supcus_guid = serializers.SerializerMethodField('get_supcus_guid')
    code = serializers.SerializerMethodField('get_code')

    def get_value(self, obj):
        return obj.supcus_guid

    def get_label(self, obj):
        return str(obj.code)+' - '+str(obj.name)
    
    def get_code(self, obj):
        return obj.code

    class Meta:
        model = RimsSupcus
        #  depth = 1
        fields = '__all__'
        '''
        fields = (
            'value',
            'label',
            'code',
            'consign',
            'accountcode',
            'type',
            'block',
            'gst_no',
            'reg_no',
            'name_reg',
            'term',   
        )
        '''
    
    def to_representation(self, instance):
        ret = super(RimsSupcusSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'selected': "false"} #if is_list_view else {'key': 'single value'}
        ret.update(extra_ret)
        return ret
    
    def validate_customer_guid(self, instance):
        check_customer_guid = super(RimsSupcusSerializer, self).to_representation(instance)
        if len(self.customer_guid) <= 0:
            raise ValidationError(
                ('Customer ID is empty')
            )
        return check_customer_guid