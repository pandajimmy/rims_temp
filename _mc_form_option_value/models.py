from django.db import models
from _mc_form_option.models import FormOption 

class FormOptionValue(models.Model):
    option_guid = models.ForeignKey(FormOption, models.DO_NOTHING, db_column='option_guid',related_name='options', verbose_name='Option guid')
    option_child_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Option Child guid')
    option_type = models.CharField(max_length=100, verbose_name='Option Type')
    option_seq = models.IntegerField(blank=True, null=True, verbose_name='Option Sequence')
    value = models.TextField(db_column='option_value')
    label = models.TextField(db_column='option_description')
    selected = models.CharField(max_length=10, db_column='option_default', verbose_name='Selected')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'form_option_value'
        ordering = ('option_seq',)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return f'/{self.label}/'  
