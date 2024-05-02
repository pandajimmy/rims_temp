from django.db import models
from _mc_design_tab.models import DesignTab 

# Create your models here.
class DesignDynamic(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    tab_guid = models.ForeignKey(DesignTab, models.DO_NOTHING, db_column='tab_guid',related_name='child_design_tab')
    isactive = models.SmallIntegerField(blank=True, null=True)
    dynamic_seq = models.SmallIntegerField(blank=True, null=True)
    dynamic_value = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_dynamic'
        ordering = ('dynamic_seq',)
    
    def __str__(self):
        return str(self.dynamic_seq)

    def get_absolute_url(self):
        return f'/{self.dynamic_seq}/'  