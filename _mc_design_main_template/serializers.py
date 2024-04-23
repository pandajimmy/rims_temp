from .models import DesignMainTemplate
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_design_template.serializers import DesignTemplateSerializer
#from _mc_design_menu.serializers import DesignMenuSerializer

class DesignMainTemplateSerializer(serializers.ModelSerializer):
    
    child_design_template = DesignTemplateSerializer(many=True, read_only=True)
    #child_design_menu = DesignMenuSerializer(many=True, read_only=True)

    
    class Meta:
        model = DesignMainTemplate
 #      depth = 1
        fields = ( 
                     'customer_guid',
                     'main_guid',
                     'main_name',
                     'main_description',
                     'isactive',
                     'isdefault',
                     'child_design_template',
                     
              )