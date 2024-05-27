from django.db import models
from _mc_tta_list.models import TtaList
from _mc_get_customer_profile.models import CustomerProfile

class TtaListPurchaseNRebates(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='purchase_n_rebates')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_purchase_n_rebates_customer_profile')
    refno = models.CharField(max_length=20, editable=False, verbose_name='Reference No.')
    
    # Unconditional rebate
    unconditional_rebate_value = models.FloatField(blank=True, null=True, verbose_name='Unconditional Rebate Value')
    unconditional_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unconditional Rebate Type')
    unconditional_rebate_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unconditional Rebate Value Type')
    
    # Commission
    commission_value = models.FloatField(blank=True, null=True, verbose_name='Commission Value')
    commission_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commission Type')
    commission_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Commission Value Type')
   
    # Auto Replenishment Rebate
    auto_replenishment_rebate_value = models.FloatField(blank=True, null=True, verbose_name='Auto Replenishment Rebate Value')
    auto_replenishment_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Auto Replenishment Rebate Type')
    auto_replenishment_rebate_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Auto Replenishment Rebate Value Type')    

    # Common Assortment Rebate
    common_assortment_rebate_value = models.FloatField(blank=True, null=True, verbose_name='Common Assortment Rebate Value')
    common_assortment_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Common Assortment Rebate Type')
    common_assortment_rebate_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Common Assortment Rebate Value Type')

    # Monthly Discount
    monthly_discount_value = models.FloatField(blank=True, null=True, verbose_name='Monthly Discount Rebate Value')
    monthly_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Discount Rebate Type')
    monthly_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Discount Value Type')

    # Monthly Discount
    monthly_discount_value = models.FloatField(blank=True, null=True, verbose_name='Monthly Discount Rebate Value')
    monthly_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Discount Rebate Type')
    monthly_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Discount Value Type')

    # Target Period
    target_period_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Period Rebate Type')

    # Target Purchase Tier 1
    target_purchase_tier_1_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 1 Value 1')
    target_purchase_tier_1_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 1 Value 2')
    target_purchase_tier_1_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 1 Type 1')
    target_purchase_tier_1_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 1 Type 2')
    target_purchase_tier_1_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 1 Value Type')

    # Target Purchase Tier 2
    target_purchase_tier_2_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 2 Value 1')
    target_purchase_tier_2_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 2 Value 2')
    target_purchase_tier_2_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 2 Type 1')
    target_purchase_tier_2_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 2 Type 2')
    target_purchase_tier_2_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 2 Value Type')

    # Target Purchase Tier 3
    target_purchase_tier_3_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 3 Value 1')
    target_purchase_tier_3_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Purchase Tier 3 Value 2')
    target_purchase_tier_3_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 3 Type 1')
    target_purchase_tier_3_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 3 Type 2')
    target_purchase_tier_3_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Tier 3 Value Type')

    # Target Growth Tier 1
    target_growth_tier_1_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 1 Value 1')										
    target_growth_tier_1_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 1 Value 2')										
    target_growth_tier_1_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 1 Type 1')                                                                                										
    target_growth_tier_1_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 1 Type 2')                                                                                										
    target_growth_tier_1_type3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 1 Type 3')                                                                                										
    target_growth_tier_1_type4 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 1 Type 4')                                                                                										
    target_growth_tier_1_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 1 Value Type')										
    
    # Target Growth Tier 2
    target_growth_tier_2_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 2 Value 1')										
    target_growth_tier_2_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 2 Value 2')										
    target_growth_tier_2_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 2 Type 1')                                                                                										
    target_growth_tier_2_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 2 Type 2')                                                                                										
    target_growth_tier_2_type3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 2 Type 3')                                                                                										
    target_growth_tier_2_type4 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 2 Type 4')                                                                                										
    target_growth_tier_2_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 2 Value Type')										
    
    # Target Growth Tier 3
    target_growth_tier_3_value1 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 3 Value 1')										
    target_growth_tier_3_value2 = models.FloatField(blank=True, null=True, verbose_name='Target Growth Tier 3 Value 2')										
    target_growth_tier_3_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 3 Type 1')                                                                                										
    target_growth_tier_3_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 3 Type 2')                                                                                										
    target_growth_tier_3_type3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 3 Type 3')                                                                                										
    target_growth_tier_3_type4 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 3 Type 4')                                                                                										
    target_growth_tier_3_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Growth Tier 3 Value Type')										

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_list_purchasenrebates'
        verbose_name = 'TTA List Purchase and Rebates Detail'
        verbose_name_plural = 'TTA List Purchase and Rebates Details'
        ordering = ['list_guid__refno']

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'