from django.db import models
from _mc_design_tab.models import DesignTab 

class DesignRow(models.Model):
    tab_guid = models.ForeignKey(DesignTab, models.DO_NOTHING, db_column='tab_guid',related_name='rows', verbose_name='Tab Globally Unique Identifier')
    row_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Row Globally Unique Identifier')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    size = models.IntegerField(blank=True, null=True, verbose_name='Size')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_row'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  
