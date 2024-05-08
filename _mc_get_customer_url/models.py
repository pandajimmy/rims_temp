from django.db import models

# Create your models here.
class CustomerUrl(models.Model):
    url_guid = models.CharField(primary_key=True, max_length=32, verbose_name='URL Globally Unique Identifier')
    customer_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Customer Globally Unique Identifier')
    customer_url = models.CharField(max_length=120, blank=True, null=True, verbose_name='Customer URL')
    key = models.CharField(max_length=60, blank=True, null=True, verbose_name='Key')
    userid = models.CharField(max_length=32, blank=True, null=True, verbose_name='User ID')
    userpass = models.CharField(max_length=32, blank=True, null=True, verbose_name='User Password')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created by')

    class Meta:
        managed = False
        db_table = 'customer_url'