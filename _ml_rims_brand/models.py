from django.db import models

# Create your models here.
class RimsBrand(models.Model):
    brand_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    mcode = models.CharField(db_column='MCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rims_brand'

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return f'/{self.code}/' 