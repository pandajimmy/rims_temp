from django.db import models
from _mc_design_menu.models import DesignMenu

class DesignMenuChild(models.Model):
    design_menu_guid = models.ForeignKey(DesignMenu, models.DO_NOTHING, db_column='design_menu_guid',related_name='sub_menu')
    design_menu_child_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_menu_child'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'