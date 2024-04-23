from .models import DesignMainTemplate
from rest_framework import serializers
#from subdept.serializers import subdeptserializer


class DesignMainTemplateSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

    value = serializers.SerializerMethodField('get_value')
    label = serializers.SerializerMethodField('get_label')

    def get_value(self, obj):
        return obj.main_guid

    def get_label(self, obj):
        return obj.main_description

    class Meta:
        model = DesignMainTemplate
 #      depth = 1
        # fields = '__all__'
        fields = (
            'value',
            'label',
        )

    def to_representation(self, instance):
        ret = super(DesignMainTemplateSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'selected': "false"} #if is_list_view else {'key': 'single value'}
        ret.update(extra_ret)
        return ret