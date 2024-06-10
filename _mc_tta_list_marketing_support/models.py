from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListMarketingSupport(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='marketing_support')
    #list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    #revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_marketing_support_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Packaging Fee
    packaging_fee_value = models.FloatField(blank=True, null=True, verbose_name='Packaging Fee Value')
    packaging_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Packaging Fee Type')
    packaging_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Packaging Fee Value Type')
    
    # Loyalty Program
    loyalty_program_value = models.FloatField(blank=True, null=True, verbose_name='Loyalty Program Value')
    loyalty_program_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Loyalty Program Type')
    loyalty_program_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Loyalty Program Value Type')
    
    # Anniversary Event
    anniversary_event_value = models.FloatField(blank=True, null=True, verbose_name='Anniversary Event Value')
    anniversary_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Event Type')
    anniversary_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Event Value Type')
    anniversary_event_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Event Date To')
    anniversary_event_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Event Date From')

    # CRM Event
    crm_event_value = models.FloatField(blank=True, null=True, verbose_name='CRM Event Value')
    crm_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Type')
    crm_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Value Type')
    crm_event_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Date To')
    crm_event_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Date From')

    # Marketing Event
    marketing_event_value = models.FloatField(blank=True, null=True, verbose_name='Marketing Event Value')
    marketing_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Type')
    marketing_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Value Type')
    marketing_event_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Date To')
    marketing_event_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Date From')

    # Concourse Event
    concourse_event_value = models.FloatField(blank=True, null=True, verbose_name='Concourse Event Value')
    concourse_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Type')
    concourse_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Value Type')
    concourse_event_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Date To')
    concourse_event_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Date From')
    
    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_marketingsupport'
        verbose_name = 'TTA List Marketing Support Detail'
        verbose_name_plural = 'TTA List Marketing Support Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  
    
    def save(self, *args, **kwargs):
        print(self.customer_guid)

        # Generate a new UUID if list_guid is empty (should be set correctly by OneToOneField)
        if not self.list_guid_id:  # Using list_guid_id to check the actual value
            self.list_guid_id = panda.panda_uuid()
            self.created_at = panda.panda_today()
            self.created_by = self.created_by or "system"  # Default to 'system' if created_by is None

        # Fetch the related TtaList object
        tta_list = TtaList.objects.get(pk=self.list_guid_id)
        new_refno = tta_list.refno

        # Only update refno if it's empty
        if not self.refno:
            self.refno = new_refno

        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by or "system"  # Default to 'system' if updated_by is None

        super(TtaListMarketingSupport, self).save(*args, **kwargs)