from django.db import models
from _mc_design_column.models import DesignColumn

class DesignComponent(models.Model):
    column_guid = models.ForeignKey(DesignColumn, models.DO_NOTHING, db_column='column_guid',related_name='components')
    component_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    offset_cols_size = models.IntegerField(blank=True, null=True)
    offset_sm_size = models.IntegerField(blank=True, null=True)
    offset_md_size = models.IntegerField(blank=True, null=True)
    offset_lg_size = models.IntegerField(blank=True, null=True)
    offset_xl_size = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    input_type = models.CharField(max_length=100, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    left_label = models.CharField(max_length=100, blank=True, null=True)
    left_option_id = models.CharField(max_length=100, blank=True, null=True)
    left_option_url = models.CharField(max_length=200, blank=True, null=True)
    option_url = models.CharField(max_length=200, blank=True, null=True)
    dynamic = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_component'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  