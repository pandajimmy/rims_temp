from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class RimsBrand(models.Model):
    brand_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Brand guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='rims_brand_customer_profile')
    mcode = models.CharField(db_column='MCode', max_length=10, blank=True, null=True, verbose_name='M Code')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10, blank=True, null=True, verbose_name='Code')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True, verbose_name='Description')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rims_brand'

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return f'/{self.code}/' 