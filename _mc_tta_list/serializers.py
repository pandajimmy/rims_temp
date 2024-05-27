from .models import TtaList
from rest_framework import serializers
from rest_framework.response import Response
from _mc_tta_list_trading_brand.serializers import TtaListTradingBrandSerializer
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
        ret['exclude_outlet'] = TtaListExcludeOutletSerializer(instance.exclude_outlet, many=True).data
        ret['outlet'] = TtaListOutletSerializer(instance.outlet, many=True).data

        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'action': ""} #if is_list_view else {'key': 'single value'}
        extra_ret.update(ret)
        return extra_ret
      
      '''
        try:
            ret['purchase_n_rebates'] = TtaListPurchaseNRebatesSerializer(instance.purchase_n_rebates).data
        except TtaList.purchase_n_rebates.RelatedObjectDoesNotExist:
            ret['purchase_n_rebates'] = None

        try:
            ret['purchase_n_rebates'] = TtaListPurchaseNRebatesSerializer(instance.purchase_n_rebates).data
        except TtaList.purchase_n_rebates.RelatedObjectDoesNotExist:
            ret['purchase_n_rebates'] = None

        try:
            ret['payment_n_discount'] = TtaListPaymentNDiscountSerializer(instance.payment_n_discount).data
        except TtaList.payment_n_discount.RelatedObjectDoesNotExist:
            ret['payment_n_discount'] = None

        try:
            ret['stock_n_deliveries'] = TtaListStockNDeliveriesSerializer(instance.stock_n_deliveries).data
        except TtaList.stock_n_deliveries.RelatedObjectDoesNotExist:
            ret['stock_n_deliveries'] = None

        try:
            ret['administration_fees'] = TtaListAdministrationFeesSerializer(instance.administration_fees).data
        except TtaList.administration_fees.RelatedObjectDoesNotExist:
            ret['administration_fees'] = None

        try:
            ret['business_growth_support'] = TtaListBusinessGrowthSupportSerializer(instance.business_growth_support).data
        except TtaList.business_growth_support.RelatedObjectDoesNotExist:
            ret['business_growth_support'] = None

        try:
            ret['promotion_support'] = TtaListPromotionSupportSerializer(instance.promotion_support).data
        except TtaList.promotion_support.RelatedObjectDoesNotExist:
            ret['promotion_support'] = None

        try:
            ret['display_incentive'] = TtaListDisplayIncentiveSerializer(instance.display_incentive).data
        except TtaList.display_incentive.RelatedObjectDoesNotExist:
            ret['display_incentive'] = None

        try:
            ret['display_incentive_table'] = TtaListDisplayIncentiveTableSerializer(instance.display_incentive_table, many=True).data
        except TtaList.display_incentive_table.RelatedObjectDoesNotExist:
            ret['display_incentive_table'] = None

        try:
            ret['marketing_support'] = TtaListMarketingSupportSerializer(instance.marketing_support).data
        except TtaList.marketing_support.RelatedObjectDoesNotExist:
            ret['marketing_support'] = None

        try:
            ret['e_commerce_support'] = TtaListECommerceSupportSerializer(instance.e_commerce_support).data
        except TtaList.e_commerce_support.RelatedObjectDoesNotExist:
            ret['e_commerce_support'] = None

        try:
            ret['condition_of_trade'] = TtaListConditionOfTradeSerializer(instance.condition_of_trade).data
        except TtaList.condition_of_trade.RelatedObjectDoesNotExist:
            ret['condition_of_trade'] = None
      '''
      
      #def view(request):
            # print('123')
            # return Response({"message": "Hello for today! See you tomorrow!"})