from django.db import models

class CustomerProfile(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_regno = models.CharField(max_length=30, blank=True, null=True)
    customer_gstno = models.CharField(max_length=30, blank=True, null=True)
    customer_taxcode = models.CharField(max_length=30, blank=True, null=True)
    customer_add1 = models.CharField(max_length=60, blank=True, null=True)
    customer_add2 = models.CharField(max_length=60, blank=True, null=True)
    customer_add3 = models.CharField(max_length=60, blank=True, null=True)
    customer_add4 = models.CharField(max_length=60, blank=True, null=True)
    customer_postcode = models.CharField(max_length=6, blank=True, null=True)
    customer_state = models.CharField(max_length=20, blank=True, null=True)
    customer_country = models.CharField(max_length=25, blank=True, null=True)
    customer_tel = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_profile'
        ordering = ('customer_name',)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return f'/{self.customer_name}/'  