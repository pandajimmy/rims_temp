from django.db import models
from _lib import panda
from _mc_get_customer_profile.models import CustomerProfile
from _mc_design_tab.models import DesignTab

# Create your models here.
class DesignCot(models.Model):
    #cot_guid = models.CharField(primary_key=True, max_length=32)
    cot_guid = models.CharField(primary_key=True, max_length=32, default=panda.panda_uuid, editable=False, verbose_name='COT guid')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='cot_customer_profile')
    tab_guid = models.OneToOneField(DesignTab, on_delete=models.DO_NOTHING, db_column='tab_guid', verbose_name='Tab guid', related_name='cot_design_tab')
    cot_group = models.CharField(max_length=120, blank=True, null=True, verbose_name='COT Group')
    cot_seq = models.SmallIntegerField(blank=True, null=True, verbose_name='COT Sequence')
    cot_description = models.CharField(max_length=120, blank=True, null=True, verbose_name='COT Description')
    cot_value = models.TextField(blank=True, null=True, verbose_name='COT Value')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    isdeleted = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Deleted')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_cot'
        unique_together = (('cot_guid', 'customer_guid', 'tab_guid'),)

    def __str__(self):
        return self.cot_guid

    def get_absolute_url(self):
        return f'/{self.cot_guid}/' 
    
