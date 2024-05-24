from django.db import models
from _mc_get_customer_profile.models import CustomerProfile
from _lib import panda

# Create your models here.
class TtaListStatusTrans(models.Model):
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='ts_tta_status_trans_customer_profile')
    list_guid = models.CharField(max_length=32, verbose_name='List guid', blank=True, null=True)
    trans_guid = models.CharField(primary_key=True, max_length=32, editable=False, verbose_name='Transaction guid')
    status_key = models.CharField(max_length=30, verbose_name='Status Key', blank=True, null=True)
    status_description = models.CharField(max_length=32, verbose_name='Status Description', blank=True, null=True)
    status_process = models.CharField(max_length=60, verbose_name='Status Process', blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='Status', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created at', blank=True, null=True)
    created_by = models.CharField(max_length=100, verbose_name='Created by', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', blank=True, null=True)
    updated_by = models.CharField(max_length=100, verbose_name='Updated by', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'tta_list_status_trans'
        
    def save(self, *args, **kwargs):
        print(self.customer_guid)
        
        if self.trans_guid == '':
            self.trans_guid = panda.panda_uuid()
        
        self.created_at = panda.panda_today()
        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by
        super(TtaListStatusTrans, self).save(*args, **kwargs)
