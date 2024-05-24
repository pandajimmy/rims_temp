from django.db import models
from _mc_get_customer_profile.models import CustomerProfile
from _mc_tta_list.models import TtaList

# Create your models here.
class RimsCustomerData(models.Model):
    data_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Data guid')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='rims_customer_data_customer_profile')
    list_guid = models.OneToOneField(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='rims_customer_data_tta_list')
    module_type = models.CharField(max_length=60, blank=True, null=True, verbose_name='Module Type')
    date_from = models.DateField(blank=True, null=True, verbose_name='Date From')
    date_to = models.DateField(blank=True, null=True, verbose_name='Date To')
    data_json = models.JSONField(blank=True, null=True, verbose_name='Data JSON')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated By')

    class Meta:
        managed = False
        db_table = 'rims_customer_data'
        #unique_together = (('customer_guid', 'module_type', 'period_code'),)
