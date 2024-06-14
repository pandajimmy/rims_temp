from django.db import models
from _lib import panda
from _mc_get_customer_profile.models import CustomerProfile
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from datetime import datetime
import uuid

# Create your models here.
class RimsCpSetBranchLocation(models.Model):
    cp_set_branch_location_guid = models.CharField(primary_key=True, max_length=32, editable=False, verbose_name='Location guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='rims_cp_set_branch_location_customer_profile')
    branch_guid = models.ForeignKey(RimsCpSetBranch, on_delete=models.DO_NOTHING, db_column='BRANCH_GUID', verbose_name='Branch guid', related_name='rims_cp_set_branch_location_branch_guid')
    #branch_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Branch guid')
    code = models.CharField(db_column='CODE', max_length=100, blank=True, null=True, verbose_name='Branch Code')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Description')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name='Remark')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'rims_cp_set_branch_location'
        unique_together = (('customer_guid', 'branch_guid', 'cp_set_branch_location_guid'),)
        ordering = ('customer_guid','code')

    def __str__(self):
        return self.cp_set_branch_location_guid

    def get_absolute_url(self):
        return f'/{self.cp_set_branch_location_guid}/' 
    
    def save(self, *args, **kwargs):
        print(self.customer_guid)
        
        uuid = panda.panda_uuid()

        if self.cp_set_branch_location_guid =='':
            self.cp_set_branch_location_guid = uuid
            self.created_at=panda.panda_today()
            self.created_by = self.created_by  or "system"  # Default to 'system' if created_by is None

        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by  or "system"  # Default to 'system' if created_by is None
        super(RimsCpSetBranchLocation, self).save(*args, **kwargs)
