from django.db import models
from _mc_form_option.models import FormOption 

class FormOptionValue(models.Model):
    option_guid = models.ForeignKey(FormOption, models.DO_NOTHING, db_column='option_guid',related_name='options')
    option_child_guid = models.CharField(primary_key=True, max_length=32)
    option_type = models.CharField(max_length=100)
    option_seq = models.IntegerField(blank=True, null=True)
    value = models.TextField(db_column='option_value')
    label = models.TextField(db_column='option_description')
    selected = models.CharField(max_length=10, db_column='option_default')
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_option_value'
        ordering = ('option_seq',)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return f'/{self.label}/'  
