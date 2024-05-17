from django.db import models

# Create your models here.
class AccInternal(models.Model):
    trans_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Transaction guid')
    internal_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Internal Name')
    internal_url = models.CharField(max_length=120, blank=True, null=True, verbose_name='Internal URL Link')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created by')

    class Meta:
        managed = False
        db_table = 'acc_internal'