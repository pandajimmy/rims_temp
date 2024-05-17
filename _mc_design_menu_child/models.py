from django.db import models
from _mc_design_menu.models import DesignMenu

class DesignMenuChild(models.Model):
    design_menu_guid = models.ForeignKey(DesignMenu, models.DO_NOTHING, db_column='design_menu_guid',related_name='sub_menu', verbose_name='Design Menu guid')
    design_menu_child_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Design Menu Child guid')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Description')
    url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Url link')
    isactive = models.IntegerField(blank=True, null=True, verbose_name='Is Active')    
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=200, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=200, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_menu_child'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'