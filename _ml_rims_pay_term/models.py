from django.db import models

# Create your models here.
class RimsPayTerm(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Customer guid')
    code = models.CharField(db_column='Code', max_length=15, verbose_name='Code')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True, verbose_name='Description')  # Field name made lowercase.
    setactive = models.SmallIntegerField(db_column='SetActive', blank=True, null=True, verbose_name='Set Active')  # Field name made lowercase.
    imported_at = models.DateTimeField(blank=True, null=True, verbose_name='Imported at')
    sync_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Sync guid')

    class Meta:
        managed = False
        db_table = 'rims_pay_term'
        unique_together = (('customer_guid', 'code'),)
        ordering = ('customer_guid','description')
    
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/' 



