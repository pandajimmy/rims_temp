from django.db import models
from _lib import panda

class RimsAccCode(models.Model):
    acc_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Account Globally Unique Identifier')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer Globally Unique Identifier')
    acc_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='Account Type')
    tta_field = models.CharField(max_length=32, blank=True, null=True, verbose_name='TTA Field')
    tta_description = models.CharField(max_length=60, blank=True, null=True, verbose_name='TTA Description')
    acc_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Account Code')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'rims_acc_code'
    
    def save(self, *args, **kwargs):
        if self.acc_guid == '':
            self.acc_guid = panda.panda_uuid()
        
        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by
        super(RimsAccCode, self).save(*args, **kwargs)