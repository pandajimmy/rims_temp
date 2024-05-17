from django.db import models
from _mc_design_row.models import DesignRow 

class DesignColumn(models.Model):
    row_guid = models.ForeignKey(DesignRow, models.DO_NOTHING, db_column='row_guid', related_name='columns', verbose_name='Row guid')
    column_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Column guid')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    cols_size = models.IntegerField(blank=True, null=True, verbose_name='Column Size')
    sm_size = models.IntegerField(blank=True, null=True, verbose_name='Small Size')
    md_size = models.IntegerField(blank=True, null=True, verbose_name='Medium Size')
    lg_size = models.IntegerField(blank=True, null=True, verbose_name='Large Size')
    xl_size = models.IntegerField(blank=True, null=True, verbose_name='Extra Large Size')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_column'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  