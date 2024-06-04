from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListECommerceSupport(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='e_commerce_support')
    #list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    #revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_e_commerce_support_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # E-Commerce Sales
    e_commerce_sales_value = models.FloatField(blank=True, null=True, verbose_name='E-Commerce Sales Value')
    e_commerce_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='E-Commerce Sales Type')
    e_commerce_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='E-Commerce Sales Value Type')
    e_commerce_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='E-Commerce Sales Date To')
    e_commerce_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='E-Commerce Sales Date From')
 
    # System Setup & Maintenance
    system_setup_n_maintenance_value = models.FloatField(blank=True, null=True, verbose_name='System Setup & Maintenance Value')
    system_setup_n_maintenance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup & Maintenance Type')
    system_setup_n_maintenance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup & Maintenance Value Type')
    system_setup_n_maintenance_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup & Maintenance Date To')
    system_setup_n_maintenance_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup & Maintenance Date From')
    
    # Digital Communication
    digital_communication_value = models.FloatField(blank=True, null=True, verbose_name='Digital Communication Value')
    digital_communication_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Type')
    digital_communication_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Value Type')
    digital_communication_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Date To')
    digital_communication_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Date From')
 
    # Social Media Post
    social_media_post_value = models.FloatField(blank=True, null=True, verbose_name='Social Media Post Value')
    social_media_post_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Type')
    social_media_post_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Value Type')
    social_media_post_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Date To')
    social_media_post_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Date From')
 
    # Market Place Event
    market_place_event_value = models.FloatField(blank=True, null=True, verbose_name='Market Place Event Value')
    market_place_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Type')
    market_place_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Value Type')
    market_place_event_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Date To')
    market_place_event_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Date From')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_list_ecommercesupport'
        verbose_name = 'TTA List E-Commerce Support Detail'
        verbose_name_plural = 'TTA List E-Commerce Support Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  
    
    def save(self, *args, **kwargs):
        print(self.customer_guid)
        
        uuid = panda.panda_uuid()

        if self.list_guid =='':
            self.list_guid = uuid
            self.created_at=panda.panda_today()
            self.created_by=self.created_by
            

        #allresult = Sysrun.objects.filter(customer_guid=self.customer_guid).first()
        allresult = Sysrun.objects.filter(customer_guid=self.customer_guid, type='TTA').first()
        new_refno = str(allresult.customer_prefix) + str(allresult.type) + str(allresult.yyyy)[:2] + str(allresult.mm).zfill(2) + str(allresult.nodigit).zfill(4)

        
        
        
        if self.refno == '':
            self.refno = new_refno
            t =  Sysrun.objects.get(customer_guid=self.customer_guid, type='TTA')
            t.nodigit += 1  # change field
            t.save() # this will update only

        
        self.updated_at=panda.panda_today()
        self.updated_by=self.updated_by
        super(TtaListECommerceSupport,self).save(*args, **kwargs)