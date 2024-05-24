from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListPaymentNDiscount(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='payment_n_discount')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    discount_guid = models.CharField(max_length=36, blank=True, null=False, editable=False, verbose_name='Discount guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_payment_n_discount_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Payment Terms
    payment_terms_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Payment Terms Type')
    
    # Early Payment Terms
    early_payment_terms_value = models.FloatField(blank=True, null=True, verbose_name='Early Payment Terms Value')
    early_payment_terms_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Terms Type')										

    # Early Payment Discount
    early_payment_discount_value = models.FloatField(blank=True, null=True, verbose_name='Early Payment Discount Value')
    early_payment_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Type')		
    early_payment_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Value Type')		

    # Prompt Payment Discount
    prompt_payment_discount_value = models.FloatField(blank=True, null=True, verbose_name='Prompt Payment Discount Value')
    prompt_payment_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Prompt Payment Discount Type')		
    prompt_payment_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Prompt Payment Discount Value Type')		

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_list_paymentndiscount'
        verbose_name = 'TTA List Payment and Discount Detail'
        verbose_name_plural = 'TTA List Payment and Discount Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  