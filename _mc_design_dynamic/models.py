from django.db import models
from _mc_design_tab.models import DesignTab 
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class DesignDynamic(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Dynamic guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='design_dynamic_customer_profile')
    tab_guid = models.ForeignKey(DesignTab, models.DO_NOTHING, db_column='tab_guid',related_name='child_design_tab', verbose_name='Tab guid')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    dynamic_seq = models.SmallIntegerField(blank=True, null=True, verbose_name='Dynamic sequence')
    dynamic_value = models.JSONField(blank=True, null=True, verbose_name='Dynamic value')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_dynamic'
        ordering = ('dynamic_seq',)
    
    def __str__(self):
        return str(self.dynamic_seq)

    def get_absolute_url(self):
        return f'/{self.dynamic_seq}/'  