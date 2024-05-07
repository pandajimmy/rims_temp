from django.db import models
from _mc_design_column.models import DesignColumn

class DesignComponent(models.Model):
    column_guid = models.ForeignKey(DesignColumn, models.DO_NOTHING, db_column='column_guid',related_name='components', verbose_name='Column Globally Unique Identifier')
    component_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Component Globally Unique Identifier')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    cols_size = models.IntegerField(blank=True, null=True, verbose_name='Column Size')
    sm_size = models.IntegerField(blank=True, null=True, verbose_name='Small Size')
    md_size = models.IntegerField(blank=True, null=True, verbose_name='Medium Size')
    lg_size = models.IntegerField(blank=True, null=True, verbose_name='Large Size')
    xl_size = models.IntegerField(blank=True, null=True, verbose_name='Extra Large Size')
    offset_cols_size = models.IntegerField(blank=True, null=True, verbose_name='Offset Column Size')
    offset_sm_size = models.IntegerField(blank=True, null=True, verbose_name='Offset Small Size')
    offset_md_size = models.IntegerField(blank=True, null=True, verbose_name='Offset Medium Size')
    offset_lg_size = models.IntegerField(blank=True, null=True, verbose_name='Offset Large Size')
    offset_xl_size = models.IntegerField(blank=True, null=True, verbose_name='Offset Extra Large Size')
    group = models.CharField(max_length=200, blank=True, null=True, verbose_name='Group')
    input_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Input Type')
    rows = models.IntegerField(blank=True, null=True, verbose_name='Rows')
    id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Identifier')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    placeholder = models.CharField(max_length=100, blank=True, null=True, verbose_name='Placeholder')
    text = models.CharField(max_length=200, blank=True, null=True, verbose_name='Text')
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Type')
    left_label = models.CharField(max_length=100, blank=True, null=True, verbose_name='Left Label')
    left_option_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Left Option Identifier')
    left_option_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Left Option Url')
    option_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Option Url')
    dynamic = models.SmallIntegerField(blank=True, null=True, verbose_name='Dynamic')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_component'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  