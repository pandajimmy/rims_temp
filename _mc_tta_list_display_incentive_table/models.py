from django.db import models
import uuid
import hashlib
from _lib import panda
from _mc_tta_list.models import TtaList 
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from _mc_get_customer_profile.models import CustomerProfile

class TtaListDisplayIncentiveTable(models.Model):
    # Main Details
    tta_display_incentive_table_guid = models.CharField(primary_key=True, max_length=36, blank=True, null=False, editable=False, verbose_name='TTA List Display Incentive Table guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='display_incentive_table')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_display_incentive_table_customer_profile')

    branch_guid = models.ForeignKey(RimsCpSetBranch, on_delete=models.DO_NOTHING, db_column='branch_guid', verbose_name='Branch guid', related_name='display_incentive_table_branch')
    
    code = models.CharField(max_length=200, blank=True, null=True, verbose_name='Code')
    outlet = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet')
    percent = models.FloatField(blank=True, null=True, verbose_name='Percent')

    # Details of Creation
    
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    

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
    
    def save(self, *args, **kwargs):
        # Ensure tta_display_incentive_table_guid is set
        if not self.tta_display_incentive_table_guid:
            self.tta_display_incentive_table_guid = self.generate_unique_guid()
        
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_guid():
        def random_guid_part():
            return hashlib.md5(uuid.uuid4().bytes).hexdigest()[:8].upper()
        return ''.join(random_guid_part() for _ in range(4))