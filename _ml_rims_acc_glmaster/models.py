from django.db import models
from _lib import panda

class RimsAccGlmaster(models.Model):
    glmaster_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    acc_type = models.CharField(max_length=20, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    acc_description = models.CharField(max_length=60, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rims_acc_glmaster'
        unique_together = (('customer_guid', 'acc_code'),)
    
    def save(self, *args, **kwargs):
        if self.glmaster_guid == '':
            self.glmaster_guid = panda.panda_uuid()
        
        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by
        super(RimsAccGlmaster, self).save(*args, **kwargs)
