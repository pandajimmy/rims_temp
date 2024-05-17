from django.db import models

class CustomerProfileTable(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Customer guid')
    customer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Customer Name')
    customer_regno = models.CharField(max_length=30, blank=True, null=True, verbose_name='Customer Registration No.')
    customer_gstno = models.CharField(max_length=30, blank=True, null=True, verbose_name='Customer GST No.')
    customer_taxcode = models.CharField(max_length=30, blank=True, null=True, verbose_name='Customer Tax Code')
    customer_add1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Customer Address 1')
    customer_add2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Customer Address 2')
    customer_add3 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Customer Address 3')
    customer_add4 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Customer Address 4')
    customer_postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name='Customer Postcode')
    customer_state = models.CharField(max_length=20, blank=True, null=True, verbose_name='Customer State')
    customer_country = models.CharField(max_length=25, blank=True, null=True, verbose_name='Customer Country')
    customer_tel = models.CharField(max_length=50, blank=True, null=True, verbose_name='Customer Tel No.')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'customer_profile'
        ordering = ('customer_name',)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return f'/{self.customer_name}/'  