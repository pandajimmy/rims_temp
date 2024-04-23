from django.db import models
from _mc_design_row.models import DesignRow 

class DesignColumn(models.Model):
    row_guid = models.ForeignKey(DesignRow, models.DO_NOTHING, db_column='row_guid',related_name='columns')
    column_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_column'
        ordering = ('seq',)

    def __str__(self):
        return self.seq

    def get_absolute_url(self):
        return f'/{self.seq}/'  