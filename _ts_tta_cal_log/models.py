from django.db import models
from _lib import panda

# Create your models here.
class TtaListCalLogs(models.Model):
    log_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    list_guid = models.CharField(max_length=32)
    log_module = models.CharField(max_length=255, blank=True, null=True)
    log_ref = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=60, blank=True, null=True)
    log_json = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

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