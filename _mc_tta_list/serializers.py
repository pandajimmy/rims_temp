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
        
      # Accessing brand_code from the related TtaListTradingBrand instance
        trading_brand_instance = instance.trading_brand_list.first()  # Assuming there's only one related trading brand
        if trading_brand_instance:
            ret['brand_code'] = trading_brand_instance.brand_code
        else:
            ret['brand_code'] = None  # Handle case where no related trading brand exists
        
        # Tta Details
        ret['trading_brand_list'] = TtaListTradingBrandSerializer(instance.trading_brand_list, many=True).data
        ret['purchase_n_rebates_list'] = TtaListPurchaseNRebatesSerializer(instance.purchase_n_rebates_list).data
        ret['payment_n_discount_list'] = TtaListPaymentNDiscountSerializer(instance.payment_n_discount_list).data
        ret['stock_n_deliveries_list'] = TtaListStockNDeliveriesSerializer(instance.stock_n_deliveries_list).data
        ret['administration_fees_list'] = TtaListAdministrationFeesSerializer(instance.administration_fees_list).data
        ret['business_growth_support_list'] = TtaListBusinessGrowthSupportSerializer(instance.business_growth_support_list).data
        ret['promotion_support_list'] = TtaListPromotionSupportSerializer(instance.promotion_support_list).data
        ret['display_incentive_list'] = TtaListDisplayIncentiveSerializer(instance.display_incentive_list).data
        ret['marketing_support_list'] = TtaListMarketingSupportSerializer(instance.marketing_support_list).data
        ret['e_commerce_support_list'] = TtaListECommerceSupportSerializer(instance.e_commerce_support_list).data
        ret['condition_of_trade_list'] = TtaListConditionOfTradeSerializer(instance.condition_of_trade_list).data

        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret
      
      #def view(request):
            # print('123')
            # return Response({"message": "Hello for today! See you tomorrow!"})