from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model

class TtaListConditionOfTrade(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='condition_of_trade')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    condition_guid = models.CharField(max_length=36, blank=True, null=False, editable=False, verbose_name='Condition of Trade guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer guid')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Condition Of Trade Type
    cot_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Condition of Trade Type')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_conditionoftrade'
        verbose_name = 'TTA List Condition Of Trade Detail'
        verbose_name_plural = 'TTA List Condition Of Trade Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  