from django.db import models
from _mc_design_template.models import DesignTemplate

class DesignTab(models.Model):
    template_guid = models.ForeignKey(DesignTemplate, models.DO_NOTHING, db_column='template_guid', related_name='sections', verbose_name='Template Globally Unique Identifier')
    tab_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Tab Globally Unique Identifier')
    key_description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Key Description')
    description = models.CharField(max_length=30, blank=True, null=True, verbose_name= 'Description')
    sequence = models.SmallIntegerField(blank=True, null=True, verbose_name= 'Sequence')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name= 'Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name= 'Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name= 'Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name= 'Updated by')

    class Meta:
        managed = False
        db_table = 'design_tab'
        ordering = ('sequence',)

    def __str__(self):
        return str(self.sequence)

    def get_absolute_url(self):
        return f'/{self.sequence}/'  