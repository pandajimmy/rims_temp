from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListPaymentNDiscount(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name='payment_n_discount')
    #list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    #revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_payment_n_discount_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Payment Terms
    payment_terms_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Payment Terms Type')
    
    # Early Payment Terms
    early_payment_terms_value = models.FloatField(blank=True, null=True, verbose_name='Early Payment Terms Value')
    early_payment_terms_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Terms Type')										

    # Early Payment Discount
    early_payment_discount_value = models.FloatField(blank=True, null=True, verbose_name='Early Payment Discount Value')
    early_payment_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Type')		
    early_payment_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Value Type')		

    # Prompt Payment Discount
    prompt_payment_discount_value = models.FloatField(blank=True, null=True, verbose_name='Prompt Payment Discount Value')
    prompt_payment_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Prompt Payment Discount Type')		
    prompt_payment_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Prompt Payment Discount Value Type')		

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_list_paymentndiscount'
        verbose_name = 'TTA List Payment and Discount Detail'
        verbose_name_plural = 'TTA List Payment and Discount Details'
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

        if self.list_link_guid == None:
            self.list_link_guid = uuid
            self.revision = '0'
            

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
        super(TtaList,self).save(*args, **kwargs)