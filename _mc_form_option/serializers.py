from .models import FormOption
from rest_framework import serializers
#from subdept.serializers import subdeptserializer
from _mc_form_option_value.serializers import FormOptionValueSerializer

class FormOptionSerializer(serializers.ModelSerializer):
       options = FormOptionValueSerializer(many=True, read_only=True)
       class Meta:
              model = FormOption
       #      depth = 1
              # fields = '__all__'
              fields = (
                     # 'created_at',
                     # 'created_by',
                     # 'updated_at',
                     # 'updated_by',
                     # 'description',
                     # 'option_guid',
                     'option_type',
                     'options'
                     
              )
       
       # def to_representation(self, instance):
       #        data = super(FormOptionSerializer, self).to_representation(instance)

       #        main = {}
       #        child = {}
       #        for key in data:

       #               if key == 'options':
       #                      for xkey in data[key]:
                                   
       #                             d = {'options':{"language": 'select/deselect All','libs':[xkey]}}
       #                             child.update(d)
       #               else:
       #                      d = {key:data[key]}
       #                      main.update(d)

       #               main.update(child)

       #        return main