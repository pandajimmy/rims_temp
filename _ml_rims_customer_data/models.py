from django.db import models

# Create your models here.
class RimsCustomerData(models.Model):
    data_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Data Globally Unique Identifier')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer Globally Unique Identifier')
    list_guid = models.CharField(max_length=32, verbose_name='List Globally Unique Identifier')
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
