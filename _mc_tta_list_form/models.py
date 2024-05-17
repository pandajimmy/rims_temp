from django.db import models
from _mc_tta_list.models import TtaList
import uuid

def generate_uuid():
    return uuid.uuid4().hex.upper()

class TtaListForm(models.Model):
    list_guid_c = models.CharField(default=generate_uuid,primary_key=True, max_length=32, verbose_name='List guid C')
    list_guid = models.ForeignKey(TtaList, models.DO_NOTHING, db_column='list_guid', blank=True, null=True, verbose_name='List guid')
    tab_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Tab guid')
    group = models.CharField(max_length=200, blank=True, null=True, verbose_name='Group')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    key_description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Key Description')
    left_option = models.CharField(max_length=100, blank=True, null=True, verbose_name='Left Option')
    varchar_1 = models.CharField(max_length=120, blank=True, null=True, verbose_name='Var Char 1')
    type_1 = models.CharField(max_length=32, blank=True, null=True, verbose_name='Type 1')
    val_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Value 1')
    text_1 = models.TextField(blank=True, null=True, verbose_name='Text 1')
    type_2 = models.CharField(max_length=32, blank=True, null=True, verbose_name='Type 2')
    val_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Value 2')
    type_3 = models.CharField(max_length=32, blank=True, null=True, verbose_name='Type 3')
    val_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True, verbose_name='Value 3')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_list_form'
        ordering = ('group',)

    def __str__(self):
        return self.group

    def get_absolute_url(self):
        return f'/{self.group}/'  