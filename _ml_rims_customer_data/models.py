from django.db import models

# Create your models here.
class RimsCustomerData(models.Model):
    data_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    list_guid = models.CharField(max_length=32)
    module_type = models.CharField(max_length=60, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    data_json = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rims_customer_data'
        #unique_together = (('customer_guid', 'module_type', 'period_code'),)
