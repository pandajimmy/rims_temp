from django.db import models
import uuid
from _lib import panda

class TtaLogs(models.Model):
    log_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Log guid')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer guid')
    log_module = models.CharField(max_length=255, blank=True, null=True, verbose_name='Log Module')
    log_ref = models.CharField(max_length=60, blank=True, null=True, verbose_name='Log Reference')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=60, blank=True, null=True, verbose_name='Created by')
    log_json = models.JSONField(blank=True, null=True, verbose_name='Log JSON')
    remark = models.JSONField(blank=True, null=True, verbose_name='Remark')

    class Meta:
        managed = False
        db_table = 'tta_logs'
        ordering = ('log_guid', 'log_ref')

    def __str__(self):
        return self.log_guid

    def get_absolute_url(self):
        return f'/{self.log_guid}/'

    def save(self, *args, **kwargs):
        if self.log_guid == '':
            self.log_guid = panda.panda_uuid()

        self.created_at = panda.panda_today()
        super(TtaLogs, self).save(*args, **kwargs)
