from django.db import models
from _mc_design_template.models import DesignTemplate

class DesignTab(models.Model):
    template_guid = models.ForeignKey(DesignTemplate, models.DO_NOTHING, db_column='template_guid',related_name='sections')
    tab_guid = models.CharField(primary_key=True, max_length=32)
    key_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    sequence = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_tab'
        ordering = ('sequence',)

    def __str__(self):
        return self.sequence

    def get_absolute_url(self):
        return f'/{self.sequence}/'  