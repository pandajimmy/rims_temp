from .models import TtaListPurchaseNRebates
from rest_framework import serializers
# from _mc_tta_list.serializers import TtaListSerializer
#from subdept.serializers import subdeptserializer


class TtaListPurchaseNRebatesSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

    # tta_list = TtaListSerializer(read_only=True, source='list_guid')
   
    class Meta:
        model = TtaListPurchaseNRebates
 #      depth = 1
        fields = '__all__'