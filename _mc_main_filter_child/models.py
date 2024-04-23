from django.db import models
from _mc_main_filter.models import MainFilter

class MainFilterChild(models.Model):
    main_filter_guid = models.ForeignKey(MainFilter, models.DO_NOTHING, db_column='main_filter_guid',related_name='child_filter_type')
    child_filter_guid = models.CharField(primary_key=True, max_length=32)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    parameter = models.CharField(max_length=100, blank=True, null=True)
    seq = models.SmallIntegerField(blank=True, null=True)
    option_type = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_filter_child'
        ordering = ('seq',)

    def __str__(self):
        return self.option_type

    def get_absolute_url(self):
        return f'/{self.option_type}/'  