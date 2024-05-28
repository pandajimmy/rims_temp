import uuid
import hashlib
from django.db import models
from _mc_tta_list.models import TtaList 
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from _mc_get_customer_profile.models import CustomerProfile

class TtaListExcludeOutlet(models.Model):
    # Main Details
    tta_exclude_outlet_guid = models.CharField(primary_key=True, max_length=32, blank=True, null=False, editable=False, verbose_name='TTA List Exclude Outlet guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='exclude_outlet')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_exclude_outlet_customer_profile')

    branch_guid = models.ForeignKey(RimsCpSetBranch, on_delete=models.DO_NOTHING, db_column='branch_guid', verbose_name='Branch guid', related_name='exclude_outlet_branch')
    outlet = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet')

    # Details of Creation
    '''
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    '''

    class Meta:
        managed = False
        db_table = 'tta_list_excludeoutlet'
        verbose_name = 'TTA List Exclude Outlet Detail'
        verbose_name_plural = 'TTA List Exclude Outlet Details'
        ordering = ('list_guid',)

    def __str__(self):
        return self.list_guid

    def get_absolute_url(self):
        return f'/{self.list_guid}/'

    def save(self, *args, **kwargs):
        # Ensure tta_exclude_outlet_guid is set
        if not self.tta_exclude_outlet_guid:
            self.tta_exclude_outlet_guid = self.generate_unique_guid()
        
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_guid():
        def random_guid_part():
            return hashlib.md5(uuid.uuid4().bytes).hexdigest()[:8].upper()
        return ''.join(random_guid_part() for _ in range(4))