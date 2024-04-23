from .models import DesignTemplate
from rest_framework import serializers
from _mc_design_tab.serializers import DesignTabSerializer


class DesignTemplateSerializer(serializers.ModelSerializer):
       sections = DesignTabSerializer(many=True, read_only=True)
       class Meta:
              model = DesignTemplate
       #      depth = 1
              # fields = 1
              # fields = '__all__'
              fields = (
                     'main_guid',
                     # 'template_guid',
                     # 'description',
                     'description',
                     'sections',
                     #'customer_guid',
                     )