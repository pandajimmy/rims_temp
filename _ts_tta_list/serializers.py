from .models import TtaList_ts
from rest_framework import serializers
from django.db import connection
#from subdept.serializers import subdeptserializer


class TtaList_tsSerializer(serializers.ModelSerializer):
      
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)
      class Meta:
            model = TtaList_ts
            #      depth = 1
            fields = '__all__'
            # fields = (
            #       'list_guid',
            #       'customer_guid',
            #       'refno',
            #       'supplier_guid',
            #       'supplier_code',
            #       'supplier_name',
            #       'bill_supp_guid',
            #       'bill_supp_code',
            #       'bill_supp_name',
            #       'negotiation_year',
            #       'co_reg_no',
            #       'tta_period_from',
            #       'trading_type',
            #       'delivery_mode',
            #       'returnable',
            #       'supplier_pic',
            #       'supplier_pic_name',
            #       'supplier_pic_position',
            #       'supplier_pic_contact',
            #       'supplier_pic_email',
            #       'banner',
            #       'outlet',
            #       'supplier_profile',
            #       'stock_n_deliveries',
            #       'administration_fees',
            #       'business_growth_support',
            #       'promotion_support',
            #       'display_incentive',
            #       'marketing_support',
            #       'e_commerce_support',
            #       'concess_n_consign',
            #       'data_sharing_plan',
            #       'condition_of_trade',
            #       'effective_date',
            #       'created_at',
            #       'created_by',
            #       'updated_at',
            #       'updated_by',
            #       'submit_date',
            #       'submit_by',
            #       'approve_date',
            #       'approve_by',
            #       'reject_at',
            #       'reject_by',
            #       'list_status',
            #       'ecommerce_support',
            #       'purchase_rebate_tier'
            # )
            

      def to_representation(self, instance):
            # cursor = connection.cursor()
            # cursor.execute("SET sort_buffer_size = 262144256000000")
            ret = super(TtaList_tsSerializer, self).to_representation(instance)
            # check the request is list view or detail view
            is_list_view = isinstance(self.instance, list)
            extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
            extra_ret.update(ret)
            return extra_ret