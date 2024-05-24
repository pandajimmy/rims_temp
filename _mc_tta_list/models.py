from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.db import connection
from _mc_get_customer_profile.models import CustomerProfile

#from django import forms
# def generate_uuid():
#     return uuid.uuid4().hex.upper()

class TtaList(models.Model):
    #list_guid = models.CharField(default=generate_uuid,primary_key=True, max_length=32)
    list_guid = models.CharField(primary_key=True, max_length=32,editable=False, verbose_name='List guid')
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_list_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')
    
    # Supplier Profile
    supplier_guid = models.CharField(max_length=32, verbose_name='Supplier guid')
    supplier_code = models.CharField(max_length=15, blank=True, null=True, verbose_name='Supplier Code')
    supplier_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier Name')
    bill_supp_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Bill Supplier guid')
    bill_supp_code = models.CharField(max_length=15, blank=True, null=True, verbose_name='Bill Supplier Code')
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Bill Supplier Name')
    
    # New Columns
    supplier_add1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Address 1')
    supplier_add2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Address 2')
    supplier_add3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Address 3')
    supplier_add4 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Address 4')
    supplier_add5 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Address 5')
    supplier_telno = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Tel No.')
    supplier_faxno = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Fax No.')
    
    negotiation_year = models.TextField(blank=True, null=True, verbose_name='Negotiation Year')  # This field type is a guess.
    co_reg_no = models.CharField(max_length=32,blank=True, null=True, verbose_name='Company Registration No.')
    tta_period_from = models.CharField(max_length=32, blank=True, null=True, verbose_name='Tta Period From')
    tta_period_to = models.CharField(max_length=32, blank=True, null=True, verbose_name='Tta Period To')
    internal_pic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Internal PIC')
    trading_group1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Trading Group 1')
    trading_group2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Trading Group 2')    
    trading_type = models.CharField(max_length=60, blank=True, null=True, verbose_name='Trading Type')
    delivery_mode = models.CharField(max_length=60, blank=True, null=True, verbose_name='Delivery Mode')
    returnable = models.CharField(max_length=10, blank=True, null=True, verbose_name='Returnable')
    supplier_pic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier PIC')
    supplier_pic_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier PIC Name')
    supplier_pic_position = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier PIC Position')
    supplier_pic_contact = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier PIC Contact')
    supplier_pic_email = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier PIC Email')
    banner = models.TextField(blank=True, null=True, verbose_name='Banner')
    outlet1 = models.TextField(blank=True, null=True, verbose_name='Outlet1')
    outlet2 = models.TextField(blank=True, null=True, verbose_name='Outlet2')
    
    '''
    supplier_profile = models.JSONField(blank=True, null=True, verbose_name='Supplier Profile')
    purchase_n_rebates = models.JSONField(blank=True, null=True, verbose_name='Purchase and Rebates')
    payment_n_discount = models.JSONField(blank=True, null=True, verbose_name='Payment and Discount')
    stock_n_deliveries = models.JSONField(blank=True, null=True, verbose_name='Stock and Deliveries')
    administration_fees = models.JSONField(blank=True, null=True, verbose_name='Administration Fees')
    business_growth_support = models.JSONField(blank=True, null=True, verbose_name='Business Growth Support')
    promotion_support = models.JSONField(blank=True, null=True, verbose_name='Promotion Support')
    display_incentive = models.JSONField(blank=True, null=True, verbose_name='Display Incentive')
    marketing_support = models.JSONField(blank=True, null=True, verbose_name='Marketing Support')
    e_commerce_support = models.JSONField(blank=True, null=True, verbose_name='E Commerce Support')
    concess_n_consign = models.JSONField(blank=True, null=True, verbose_name='Concess and Consign')
    data_sharing_plan = models.JSONField(blank=True, null=True, verbose_name='Data Sharing Plan')
    condition_of_trade = models.JSONField(blank=True, null=True, verbose_name='Condition of Trade')
    effective_date = models.CharField(max_length=32, blank=True, null=True, verbose_name='Effective Date')
    '''
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    submit_date = models.DateTimeField(blank=True, null=True, verbose_name='Submit Date')
    submit_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Submit by')
    approve_date = models.DateTimeField(blank=True, null=True, verbose_name='Approve Date')
    approve_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Approve by')
    reject_at = models.DateTimeField(blank=True, null=True, verbose_name='Reject at')
    reject_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Reject by')
    list_status = models.CharField(max_length=20, blank=True, null=True, verbose_name='List Status')
    # ecommerce_support = models.JSONField(blank=True, null=True, verbose_name='Ecommerce Support')
    # purchase_rebate_tier = models.JSONField(blank=True, null=True, verbose_name='Purchase Rebate Tier')

    class Meta:
        managed = False
        db_table = 'tta_list'
        ordering = ('refno','list_guid')

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