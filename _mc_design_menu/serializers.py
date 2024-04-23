from .models import DesignMenu
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_design_menu_child.serializers import DesignMenuChildSerializer

class DesignMenuSerializer(serializers.ModelSerializer):
       sub_menu = DesignMenuChildSerializer(many=True, read_only=True)
       class Meta:
              model = DesignMenu
       #      depth = 1
              fields = '__all__'