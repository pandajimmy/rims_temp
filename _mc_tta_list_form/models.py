from django.db import models
from _mc_tta_list.models import TtaList
import uuid

def generate_uuid():
    return uuid.uuid4().hex.upper()

class TtaListForm(models.Model):
    list_guid_c = models.CharField(default=generate_uuid,primary_key=True, max_length=32)
    list_guid = models.ForeignKey(TtaList, models.DO_NOTHING, db_column='list_guid', blank=True, null=True)
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    key_description = models.CharField(max_length=100, blank=True, null=True)
    left_option = models.CharField(max_length=100, blank=True, null=True)
    varchar_1 = models.CharField(max_length=120, blank=True, null=True)
    type_1 = models.CharField(max_length=32, blank=True, null=True)
    val_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    text_1 = models.TextField(blank=True, null=True)
    type_2 = models.CharField(max_length=32, blank=True, null=True)
    val_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    type_3 = models.CharField(max_length=32, blank=True, null=True)
    val_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tta_list_form'
        ordering = ('group',)

    def __str__(self):
        return self.group

    def get_absolute_url(self):
        return f'/{self.group}/'  