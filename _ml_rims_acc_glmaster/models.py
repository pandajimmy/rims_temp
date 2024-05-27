from django.db import models
from _lib import panda
from _mc_get_customer_profile.models import CustomerProfile

class RimsAccGlmaster(models.Model):
    glmaster_guid = models.CharField(primary_key=True, max_length=32, verbose_name='GL Master guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='acc_glmaster_customer_profile')
    acc_type = models.CharField(max_length=20, blank=True, null=True, verbose_name='Account Type')
    acc_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Account Code')
    acc_description = models.CharField(max_length=60, blank=True, null=True, verbose_name='Account Description')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated By')

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
