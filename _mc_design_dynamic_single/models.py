from django.db import models
from _mc_get_customer_profile.models import CustomerProfile
from _mc_design_tab.models import DesignTab
from _lib import panda

# Create your models here.
class DesignDynamic_S(models.Model):
    #dynamic_guid = models.CharField(primary_key=True, max_length=32)
    #dynamic_guid = models.CharField(primary_key=True, max_length=32,default=panda.panda_uuid,editable=False)
    dynamic_guid = models.CharField(primary_key=True, max_length=32,editable=False, verbose_name='Dynamic guid')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='design_dynamic_single_customer_profile')
    tab_guid = models.ForeignKey(DesignTab, on_delete=models.DO_NOTHING, db_column='tab_guid', verbose_name='Tab guid', related_name='design_dynamic_single_tab_guid')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    dynamic_seq = models.SmallIntegerField(blank=True, null=True, verbose_name='Dynamic sequence')
    dynamic_value = models.JSONField(blank=True, null=True, verbose_name='Dynamic value')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_dynamic'
        ordering = ('dynamic_seq',)
    
    def __str__(self):
        return self.dynamic_seq

    def get_absolute_url(self):
        return f'/{self.dynamic_seq}/' 

    # def save(self, *args, **kwargs):
    #     print(self.dynamic_guid)
        
    #     if self.dynamic_guid =='':
	#         self.dynamic_guid = panda.panda_uuid()

    #     #allresult = Sysrun.objects.filter(customer_guid=self.customer_guid).first()
    #     #new_refno = str(allresult.customer_prefix) + str(allresult.type) + str(allresult.yyyy)[:2] + str(allresult.mm).zfill(2) + str(allresult.nodigit).zfill(4)
        
        
    #     self.updated_at=panda.panda_today()
    #     self.updated_by=self.updated_by
    #     super(DesignDynamic_S,self).save(*args, **kwargs)

    