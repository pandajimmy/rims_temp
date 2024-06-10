from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListBusinessGrowthSupport(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='business_growth_support')
    #list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    #revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_business_growth_support_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Category Development Fund
    category_development_fund_value = models.FloatField(blank=True, null=True, verbose_name='Category Development Fund Value')
    category_development_fund_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Category Development Fund Type')
    category_development_fund_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Category Development Fund Value Type')
     
    # Business Development Fund
    business_development_fund_value = models.FloatField(blank=True, null=True, verbose_name='Business Development Fund Value')
    business_development_fund_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Business Development Fund Type')
    business_development_fund_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Business Development Fund Value Type')

    # Data Sharing Fee
    data_sharing_fee_value = models.FloatField(blank=True, null=True, verbose_name='Data Sharing Fee Value')
    data_sharing_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Fee Type')
    data_sharing_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Fee Value Type')
     
	# New Store Opening
    new_store_opening_value = models.FloatField(blank=True, null=True, verbose_name='New Store Opening Value')
    new_store_opening_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Type')
    new_store_opening_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Value Type')
    new_store_opening_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Date To')
    new_store_opening_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Date From')

	# New Store First Order Discount
    new_store_first_order_discount_value1 = models.FloatField(blank=True, null=True, verbose_name='New Store First Order Discount Value 1')
    new_store_first_order_discount_value2 = models.FloatField(blank=True, null=True, verbose_name='New Store First Order Discount Value 2')
    new_store_first_order_discount_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Type 1')
    new_store_first_order_discount_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Type 2')
    new_store_first_order_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Value Type')
         
    # Refurbish Store
    refurbish_store_value = models.FloatField(blank=True, null=True, verbose_name='Refurbish Store Value')
    refurbish_store_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Type')
    refurbish_store_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Value Type')
    refurbish_store_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Date To')
    refurbish_store_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Date From')

    # Anniversary Sales Allowance
    anniversary_sales_allowance_value = models.FloatField(blank=True, null=True, verbose_name='Anniversary Sales Allowance Value')
    anniversary_sales_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Type')
    anniversary_sales_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Value Type')     
    anniversary_sales_allowance_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Date To')
    anniversary_sales_allowance_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Date From')

    # Anniversary Orders Rebate
    anniversary_orders_rebate_value = models.FloatField(blank=True, null=True, verbose_name='Anniversary Orders Rebate Value')
    anniversary_orders_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Type')
    anniversary_orders_rebate_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Value Type')       
    anniversary_orders_rebate_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Date To')
    anniversary_orders_rebate_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Date From')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_businessgrowthsupport'
        verbose_name = 'TTA List Business Growth Support Detail'
        verbose_name_plural = 'TTA List Business Growth Support Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  
    
    def save(self, *args, **kwargs):
        print(self.customer_guid)

        # Generate a new UUID if list_guid is empty (should be set correctly by OneToOneField)
        if not self.list_guid_id:  # Using list_guid_id to check the actual value
            self.list_guid_id = panda.panda_uuid()
            self.created_at = panda.panda_today()
            self.created_by = self.created_by or "system"  # Default to 'system' if created_by is None

        # Fetch the related TtaList object
        tta_list = TtaList.objects.get(pk=self.list_guid_id)
        new_refno = tta_list.refno

        # Only update refno if it's empty
        if not self.refno:
            self.refno = new_refno

        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by or "system"  # Default to 'system' if updated_by is None

        super(TtaListBusinessGrowthSupport, self).save(*args, **kwargs)