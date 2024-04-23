from django.db import models
from _mc_design_tab.models import DesignTab 

class DesignRow(models.Model):
    tab_guid = models.ForeignKey(DesignTab, models.DO_NOTHING, db_column='tab_guid',related_name='rows')
    row_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_row'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  
