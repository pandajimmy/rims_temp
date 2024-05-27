from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class RimsBanner(models.Model):
    banner_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Banner guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='rims_banner_customer_profile')
    concept_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Concept guid')
    concept = models.CharField(max_length=100, blank=True, null=True, verbose_name='Concept')
    concept_inactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Concept Inactive')
    branch_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Branch guid')
    branch = models.CharField(max_length=100, blank=True, null=True, verbose_name='Branch')
    branch_inactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Inactive Branch')

    class Meta:
        managed = False
        db_table = 'rims_banner'
        unique_together = (('banner_guid', 'customer_guid'),)
        #ordering = ('concept')

    def __str__(self):
        return self.banner_guid

    def get_absolute_url(self):
        return f'/{self.banner_guid}/' 

