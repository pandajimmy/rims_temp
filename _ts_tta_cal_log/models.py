from django.db import models
from _lib import panda
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class TtaListCalLogs(models.Model):
    log_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Log guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_cal_log_customer_profile')
    list_guid = models.CharField(max_length=32, verbose_name='List guid')
    log_module = models.CharField(max_length=255, blank=True, null=True, verbose_name='Log Module')
    log_ref = models.CharField(max_length=60, blank=True, null=True, verbose_name='Log Reference')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=60, blank=True, null=True, verbose_name='Created by')
    log_json = models.TextField(blank=True, null=True, verbose_name='Log JSON')
    remark = models.TextField(blank=True, null=True, verbose_name='Remark')

    class Meta:
        managed = False
        db_table = 'tta_list_cal_logs' 

    def __str__(self):
        return self.log_guid

    def get_absolute_url(self):
        return f'/{self.log_guid}/' 

    def save(self, *args, **kwargs):   

        self.created_at=panda.panda_today()
        self.created_by=self.created_by
        super(TtaListCalLogs,self).save(*args, **kwargs)