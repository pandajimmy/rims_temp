from django.db import models

# Create your models here.
class CustomerUrl(models.Model):
    url_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    customer_url = models.CharField(max_length=120, blank=True, null=True)
    key = models.CharField(max_length=60, blank=True, null=True)
    userid = models.CharField(max_length=32, blank=True, null=True)
    userpass = models.CharField(max_length=32, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_url'