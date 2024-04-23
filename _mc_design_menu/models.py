from django.db import models
from _mc_design_main_template.models import DesignMainTemplate

class DesignMenu(models.Model):
    main_guid = models.ForeignKey(DesignMainTemplate, models.DO_NOTHING, db_column='main_guid',related_name='child_design_menu')
    design_menu_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_menu'
        ordering = ('seq',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'  