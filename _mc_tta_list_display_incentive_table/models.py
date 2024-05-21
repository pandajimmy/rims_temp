from django.db import models
from _mc_tta_list.models import TtaList 
from _ml_rims_cp_set_branch.models import RimsCpSetBranch

class TtaListDisplayIncentiveTable(models.Model):
    # Main Details
    tta_display_incentive_table_guid = models.CharField(primary_key=True, max_length=36, blank=True, null=False, editable=False, verbose_name='TTA List Display Incentive Table guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='display_incentive_table')
    customer_guid = models.CharField(max_length= 32, verbose_name='Customer guid')

    branch_guid = models.OneToOneField(RimsCpSetBranch, on_delete=models.DO_NOTHING, db_column='branch_guid', verbose_name='Branch guid', related_name='display_incentive_table_branch_list')
    
    code = models.CharField(max_length=200, blank=True, null=True, verbose_name='Code')
    outlet = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet')
    percent = models.FloatField(blank=True, null=True, verbose_name='Percent')

    # Details of Creation
    '''
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    '''

    class Meta:
        managed = False
        db_table = 'tta_displayincentive'
        verbose_name = 'TTA List Display Incentive Table Detail'
        verbose_name_plural = 'TTA List Display Incentive Table Details'
        ordering = ('list_guid',)

    def __str__(self):
        return self.list_guid

    def get_absolute_url(self):
        return f'/{self.list_guid}/'  