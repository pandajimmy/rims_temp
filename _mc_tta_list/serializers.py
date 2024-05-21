from .models import TtaList
from rest_framework import serializers
from rest_framework.response import Response
from _mc_tta_list_trading_brand.serializers import TtaListTradingBrandSerializer
from _mc_tta_list_purchase_n_rebates.serializers import TtaListPurchaseNRebatesSerializer
from _mc_tta_list_payment_n_discount.serializers import TtaListPaymentNDiscountSerializer
from _mc_tta_list_stock_n_deliveries.serializers import TtaListStockNDeliveriesSerializer
from _mc_tta_list_administration_fees.serializers import TtaListAdministrationFeesSerializer
from _mc_tta_list_business_growth_support.serializers import TtaListBusinessGrowthSupportSerializer
from _mc_tta_list_promotion_support.serializers import TtaListPromotionSupportSerializer
from _mc_tta_list_display_incentive.serializers import TtaListDisplayIncentiveSerializer
from _mc_tta_list_display_incentive_table.serializers import TtaListDisplayIncentiveTableSerializer
from _mc_tta_list_marketing_support.serializers import TtaListMarketingSupportSerializer
from _mc_tta_list_e_commerce_support.serializers import TtaListECommerceSupportSerializer
from _mc_tta_list_condition_of_trade.serializers import TtaListConditionOfTradeSerializer
#from subdept.serializers import subdeptserializer


class TtaListSerializer(serializers.ModelSerializer):
 #       subdept_key = SubdeptSerializer(many=True, read_only=True)

      
      class Meta:
            model = TtaList
            #      depth = 1
            fields = '__all__'

      def to_representation(self, instance):
        ret = super(TtaListSerializer, self).to_representation(instance)
        
 
        # Tta Details
        ret['trading_brand'] = TtaListTradingBrandSerializer(instance.trading_brand, many=True).data
        ret['purchase_n_rebates'] = TtaListPurchaseNRebatesSerializer(instance.purchase_n_rebates).data
        ret['payment_n_discount'] = TtaListPaymentNDiscountSerializer(instance.payment_n_discount).data
        ret['stock_n_deliveries'] = TtaListStockNDeliveriesSerializer(instance.stock_n_deliveries).data
        ret['administration_fees'] = TtaListAdministrationFeesSerializer(instance.administration_fees).data
        ret['business_growth_support'] = TtaListBusinessGrowthSupportSerializer(instance.business_growth_support).data
        ret['promotion_support'] = TtaListPromotionSupportSerializer(instance.promotion_support).data
        ret['display_incentive'] = TtaListDisplayIncentiveSerializer(instance.display_incentive).data
        ret['display_incentive_table'] = TtaListDisplayIncentiveTableSerializer(instance.display_incentive_table, many=True).data
        ret['marketing_support'] = TtaListMarketingSupportSerializer(instance.marketing_support).data
        ret['e_commerce_support'] = TtaListECommerceSupportSerializer(instance.e_commerce_support).data
        ret['condition_of_trade'] = TtaListConditionOfTradeSerializer(instance.condition_of_trade).data

        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret
      
      #def view(request):
            # print('123')
            # return Response({"message": "Hello for today! See you tomorrow!"})