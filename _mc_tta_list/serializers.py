from .models import TtaList
from rest_framework import serializers
from rest_framework.response import Response
from _mc_tta_list_trading_brand.serializers import TtaListTradingBrandSerializer
from _mc_tta_list_trading_group.serializers import TtaListTradingGroupSerializer
from _mc_tta_list_outlet.serializers import TtaListOutletSerializer
from _mc_tta_list_exclude_outlet.serializers import TtaListExcludeOutletSerializer
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
 #       subdept_key = SubdeptSerializer(many=True, )

      purchase_n_rebates = TtaListPurchaseNRebatesSerializer(required=False)
      payment_n_discount = TtaListPaymentNDiscountSerializer(required=False)
      stock_n_deliveries = TtaListStockNDeliveriesSerializer(required=False)
      administration_fees = TtaListAdministrationFeesSerializer(required=False)
      business_growth_support = TtaListBusinessGrowthSupportSerializer(required=False)
      promotion_support = TtaListPromotionSupportSerializer(required=False)
      display_incentive = TtaListDisplayIncentiveSerializer(required=False)
      marketing_support = TtaListMarketingSupportSerializer(required=False)
      e_commerce_support = TtaListECommerceSupportSerializer(required=False)
      condition_of_trade = TtaListConditionOfTradeSerializer(required=False)
      
      class Meta:
            model = TtaList
            #      depth = 1
            fields = '__all__'
      
      def to_representation(self, instance):
        ret = super(TtaListSerializer, self).to_representation(instance)

        # Tta Details
        ret['trading_brand'] = TtaListTradingBrandSerializer(instance.trading_brand, many=True).data
        ret['trading_group'] = TtaListTradingGroupSerializer(instance.trading_group, many=True).data
        ret['exclude_outlet'] = TtaListExcludeOutletSerializer(instance.exclude_outlet, many=True).data
        ret['outlet'] = TtaListOutletSerializer(instance.outlet, many=True).data
        ret['display_incentive_table'] = TtaListDisplayIncentiveTableSerializer(instance.display_incentive_table, many=True).data

        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret
      
      #def view(request):
            # print('123')
            # return Response({"message": "Hello for today! See you tomorrow!"})