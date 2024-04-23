from django.db import models

# Create your models here.
class AccInternal(models.Model):
    trans_guid = models.CharField(primary_key=True, max_length=32)
    internal_name = models.CharField(max_length=60, blank=True, null=True)
    internal_url = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_internal'