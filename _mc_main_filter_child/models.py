from django.db import models
from _mc_main_filter.models import MainFilter

class MainFilterChild(models.Model):
    main_filter_guid = models.ForeignKey(MainFilter, models.DO_NOTHING, db_column='main_filter_guid',related_name='child_filter_type', verbose_name='Main Filter Globally Unique Identifier')
    child_filter_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Child Filter Globally Unique Identifier')
    cols_size = models.IntegerField(blank=True, null=True, verbose_name='Column Size')
    sm_size = models.IntegerField(blank=True, null=True, verbose_name='Small Size')
    md_size = models.IntegerField(blank=True, null=True, verbose_name='Medium Size')
    lg_size = models.IntegerField(blank=True, null=True, verbose_name='Large Size')
    xl_size = models.IntegerField(blank=True, null=True, verbose_name='Extra Large Size')
    placeholder = models.CharField(max_length=100, blank=True, null=True, verbose_name='Placeholder')
    id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Identifier')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    parameter = models.CharField(max_length=100, blank=True, null=True, verbose_name='Parameter')
    seq = models.SmallIntegerField(blank=True, null=True, verbose_name='Sequence')
    option_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Option Type')
    is_active = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'main_filter_child'
        ordering = ('seq',)

    def __str__(self):
        return self.option_type

    def get_absolute_url(self):
        return f'/{self.option_type}/'  