from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

class Sysrun(models.Model):
    sysrun_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Sysrun guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='sysrun_customer_profile')
    customer_prefix = models.CharField(max_length=5, verbose_name='Customer Prefix')
    type = models.CharField(db_column='Type', blank=True, max_length=10, verbose_name='Type')  # Field name made lowercase.
    code = models.CharField(db_column='Code', blank=True, max_length=10, verbose_name='Code')
    currentno = models.IntegerField(db_column='CurrentNo', blank=True, null=True, verbose_name='Current No.')  # Field name made lowercase.
    nodigit = models.IntegerField(db_column='NoDigit', blank=True, null=True, verbose_name='Digit No.')  # Field name made lowercase.
    yyyy = models.IntegerField(db_column='YYYY', blank=True, null=True, verbose_name='YYYY')  # Field name made lowercase.
    mm = models.IntegerField(db_column='MM', blank=True, null=True, verbose_name='MM')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True, verbose_name='Remarks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysrun'
        ordering = ('currentno',)

    def __str__(self):
        return self.currentno

    def get_absolute_url(self):
        return f'/{self.currentno}/' 