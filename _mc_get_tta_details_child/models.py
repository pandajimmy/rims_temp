from django.db import models
from _mc_get_tta_details.models import TtaListDetails

class TtaListForm(models.Model):
    list_guid_c = models.CharField(primary_key=True, max_length=32, verbose_name='List guid C')
    list_guid = models.ForeignKey(TtaListDetails, models.DO_NOTHING, db_column='list_guid',related_name='dynamic_field', verbose_name='List guid')
    tab_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Tab guid')
    group = models.CharField(max_length=200, blank=True, null=True, verbose_name='Group')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    key_description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Key Description')
    left_option = models.CharField(max_length=100, blank=True, null=True, verbose_name='Left Option')
    varchar_1 = models.CharField(max_length=120, blank=True, null=True, verbose_name='First Var Char')
    type_1 = models.CharField(max_length=32, blank=True, null=True, verbose_name='First Type')
    val_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='First Value')
    text_1 = models.TextField(blank=True, null=True, verbose_name='First Text')
    type_2 = models.CharField(max_length=32, blank=True, null=True, verbose_name='Second Type')
    val_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Second Value')
    type_3 = models.CharField(max_length=32, blank=True, null=True, verbose_name='Third Type')
    val_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Third Value')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated By')

    class Meta:
        managed = False
        db_table = 'tta_list_form'
        ordering = ('group','seq')

    def __str__(self):
        return self.key_description

    def get_absolute_url(self):
        return f'/{self.key_description}/'  
