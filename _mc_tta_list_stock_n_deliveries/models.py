from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model

class TtaListStockNDeliveries(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='stock_n_deliveries_list')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    stock_guid = models.CharField(max_length=36, blank=True, editable=False, null=False, verbose_name='Stock guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer guid')
    refno = models.CharField(max_length=20, editable=False, verbose_name='Reference No.')

    # Cross Docking Allowance
    cross_docking_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Cross Docking Allowance')
    cross_docking_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cross Docking Allowance Type')
    cross_docking_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cross Docking Allowance Value Type')
    
    # Conventional Flow Thru Allowance
    conventional_flow_thru_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Conventional Flow Thru Allowance Value')
    conventional_flow_thru_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Conventional Flow Thru Allowance Type')
    conventional_flow_thru_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Conventional Flow Thru Allowance Value Type')

    # Shrinkage Pilferage Allowance
    shrinkage_pilferage_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Shrinkange Pilferafe Allowance Value')
    shrinkage_pilferage_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Shrinkange Pilferafe Allowance Type')
    shrinkage_pilferage_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Shrinkange Pilferafe Allowance Value Type')
    
    # Non Returnable Goods Allowance
    non_returnable_goods_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Non Returnable Goods Allowance Value')
    non_returnable_goods_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non Returnable Goods Allowance Type')
    non_returnable_goods_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non Returnable Goods Allowance Value Type')
    
    # East Malaysia Orders Allowance
    east_malaysia_orders_allowance_value = models.FloatField(blank=True, null=True, verbose_name='East Malaysia Orders Allowance Value')
    east_malaysia_orders_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='East Malaysia Orders Allowance Type')
    east_malaysia_orders_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='East Malaysia Orders Allowance Value Type')
    
    # Damage Good Allowance 
    damage_good_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Damage Good Allowance Value')
    damage_good_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Damage Good Allowance Type')
    damage_good_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Damage Good Allowance Value Type')
    
    # Non Compliance Packaging Allowance 
    non_compliance_packaging_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Non-compliance Packaging Allowance')
    non_compliance_packaging_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non-compliance Packaging Allowance Type')
    non_compliance_packaging_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non-compliance Packaging Allowance Value Type')
    
    # Purchase Order Fulfillment
    purchase_order_fulfillment_value = models.FloatField(blank=True, null=True, verbose_name='Purchase Order Fulfillment Value')
    purchase_order_fulfillment_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Fulfillment Type')
    purchase_order_fulfillment_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Fulfillment Value Type')
    
    # Unfulfilled Penalty
    unfulfilled_penalty_value = models.FloatField(blank=True, null=True, verbose_name='Unfulfilled Penalty Value')
    unfulfilled_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unfulfilled Penalty Type')
    unfulfilled_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unfulfilled Penalty Value Type')
    
    # Lost of Profit Penalty
    lost_of_profit_penalty_value = models.FloatField(blank=True, null=True, verbose_name='Lost of Profit Penalty Value')
    lost_of_profit_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lost of Profit Penalty Type')
    lost_of_profit_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lost of Profit Penalty Value Type')
    
    # Purchase Order Lead Time
    purchase_order_lead_time_value = models.FloatField(blank=True, null=True, verbose_name='Purchase Order Lead Time Value')
    purchase_order_lead_time_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Lead Time Type')
    purchase_order_lead_time_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Lead Time Value Type')
    
    # Lead Time Penalty
    lead_time_penalty_value = models.FloatField(blank=True, null=True, verbose_name='Lead Time Penalty Value')
    lead_time_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lead Time Penalty Type')
    lead_time_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lead Time Penalty Value Type')
    
    # Ullarge 
    ullarge_value = models.FloatField(blank=True, null=True, verbose_name='Ullarge Value')
    ullarge_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ullarge Type')
    ullarge_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ullarge Value Type')

    # Target Service Level
    target_service_level_value = models.FloatField(blank=True, null=True, verbose_name='Target Service Level Value')
    target_service_level_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Service Level Type')
    target_service_level_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Service Level Value Type')

    # Target Service Level Unfulfilled Penalty
    target_service_level_unfulfilled_penalty_value = models.FloatField(blank=True, null=True, verbose_name='Target Service Level Unfulfilled Penalty Value')
    target_service_level_unfulfilled_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Service Level Unfulfilled Penalty Type')
    target_service_level_unfulfilled_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Service Level Unfulfilled Penalty Value Type')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_stockndeliveries'
        verbose_name = 'TTA List Stock And Delivery Detail'
        verbose_name_plural = 'TTA List Stock And Deliveries Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  