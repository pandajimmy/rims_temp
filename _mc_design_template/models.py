from django.db import models
from _mc_design_main_template.models import DesignMainTemplate

class DesignTemplate(models.Model):
    main_guid = models.ForeignKey(DesignMainTemplate, models.DO_NOTHING, db_column='main_guid', related_name='child_design_template', verbose_name='Main guid')
    template_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Template guid')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')
    json = models.JSONField(blank=True, null=True, verbose_name='Json')

    
    class Meta:
        managed = False
        db_table = 'design_template'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'  