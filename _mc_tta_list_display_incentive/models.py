from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListDisplayIncentive(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='display_incentive')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    display_guid = models.CharField(max_length=36, blank=True, null=False, editable=False, verbose_name='Display Incentive guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_display_incentive_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Incentive Type
    incentive_type_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Incentive Type Type')
    incentive_type_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Incentive Type Value Type')
    
    # Display Incentive Outlet
    display_incentive_outlet_value = models.FloatField(blank=True, null=True, verbose_name='Display Incentive Outlet Value')
    display_incentive_outlet_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Display Incentive Outlet Type')
    
    #Display Incentive Table
    # display_incentive_table_type = models.JSONField(blank=True, null=True, verbose_name='Display Incentive Table Type')
    
    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_displayincentive'
        verbose_name = 'TTA List Display Incentive Detail'
        verbose_name_plural = 'TTA List Display Incentive Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  