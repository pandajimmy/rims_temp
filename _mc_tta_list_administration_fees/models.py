from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListAdministrationFees(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='administration_fees')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_administration_fees_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Account Administration Fee
    account_administration_fee_value = models.FloatField(blank=True, null=True, verbose_name='Account Administration Fee Value')
    account_administration_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Account Administration Fee Type')
    account_administration_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Account Administration Fee Value Type')
    
    # Product Registration Fee
    product_registration_fee_value = models.FloatField(blank=True, null=True, verbose_name='Product Registration Fee Value')
    product_registration_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Product Registration Fee Type')
    product_registration_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Product Registration Fee Value Type')
    
    # SKU Replacement
    sku_replacement_value = models.FloatField(blank=True, null=True, verbose_name='SKU Replacement Value')
    sku_replacement_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='SKU Replacement Type')
    sku_replacement_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='SKU Replacement Value Type')
    
    # New Line Fee
    new_line_fee_value = models.FloatField(blank=True, null=True, verbose_name='New Line Fee Value')
    new_line_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Line Fee Type')
    new_line_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Line Fee Value Type')
    
    # New Item Listing
    new_item_listing_value = models.FloatField(blank=True, null=True, verbose_name='New Vendor Item Listing Value')
    new_item_listing_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Vendor Item Listing Type')
    new_item_listing_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Vendor Item Listing Value Type')
    
    # New Item First Order Discount
    new_item_first_order_discount_value1 = models.FloatField(blank=True, null=True, verbose_name='New Item First Order Discount Value 1')
    new_item_first_order_discount_value2 = models.FloatField(blank=True, null=True, verbose_name='New Item First Order Discount Value 2')
    new_item_first_order_discount_type1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Type 1')
    new_item_first_order_discount_type2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Type 2')
    new_item_first_order_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Value Type')
    
    # Change of Purchase Type
    change_of_purchase_type_value = models.FloatField(blank=True, null=True, verbose_name='Change of Purchase Type Value')
    change_of_purchase_type_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Change of Purchase Type Type')
    change_of_purchase_type_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Change of Purchase Type Value Type')
    
    # Vendor Information Maintenance
    maintenance_of_vendor_information_value = models.FloatField(blank=True, null=True, verbose_name='Vendor Information Maintenance Value')
    maintenance_of_vendor_information_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Vendor Information Maintenance Type')
    maintenance_of_vendor_information_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Vendor Information Maintenance Value Type')
    
    # New Vendor Creation (By Existing Vendor Barcode)
    new_vcr_barcode_value = models.FloatField(blank=True, null=True, verbose_name='New Vendor Creation (By Existing Vendor Barcode) Value')
    new_vcr_barcode_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Vendor Creation (By Existing Vendor Barcode) Type')
    new_vcr_barcode_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Vendor Creation (By Existing Vendor Barcode) Value Type')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    					
    class Meta:
        managed = False
        db_table = 'tta_list_administrationfees'
        verbose_name = 'TTA List Administration Fees Detail'
        verbose_name_plural = 'TTA List Administration Fees Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  