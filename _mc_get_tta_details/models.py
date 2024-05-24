from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

class TtaListDetails(models.Model):
    # Main Details
    list_guid = models.CharField(primary_key=True, max_length=32, verbose_name='List guid')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_details_customer_profile')
    refno = models.CharField(max_length=20, verbose_name='Reference Number')

    # Supplier ID and Name
    supplier_guid = models.CharField(max_length=32, verbose_name='Supplier guid')
    supplier_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier Name')
    
    # Bill of Supplier
    bill_supp_guid = models.CharField(max_length=32, verbose_name='Bill Supplier guid')
    bill_supp_code = models.CharField(max_length=32, verbose_name='Bill Supplier Code')
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Bill Supplier Name')

    # Other Details
    negotiation_year = models.TextField(blank=True, null=True, verbose_name='Negotiation Year')
    co_reg_no = models.CharField(max_length=32, blank=True, null=True, verbose_name='Company Registration Number')
    tta_period_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='TTA Period From')
    tta_period_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='TTA Period To')
    internal_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name='Internal PIC')
    
    # Trading Information
    trading_group1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Trading Group 1')
    trading_group2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Trading Group 2')
    trading_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Trading Type')
    delivery_mode = models.CharField(max_length=200, blank=True, null=True, verbose_name='Delivery Mode')
    returnable = models.CharField(max_length=200, blank=True, null=True, verbose_name='Returnable')
    
    # Supplier Person In Charge Information
    supplier_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge')
    supplier_pic_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Name')
    supplier_pic_position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Position')
    supplier_pic_contact = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Contact')
    supplier_pic_email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Email')
    
    #Banner
    banner = models.CharField(max_length=200, blank=True, null=True, verbose_name='Banner')

    #Outlet
    outlet1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet 1')
    outlet2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet 2')

    

    #Status of the Tta List Details
    effective_date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Effective Date')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated By')
    submit_date = models.DateTimeField(blank=True, null=True, verbose_name='Submit Date')
    submit_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Submit By')
    approve_date = models.DateTimeField(blank=True, null=True, verbose_name='Approve Date')
    approve_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Approve By')
    reject_at = models.DateTimeField(blank=True, null=True, verbose_name='Reject Date')
    reject_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Reject By')
    list_status = models.CharField(max_length=20, blank=True, null=True, verbose_name='List Status')

    class Meta:
        managed = False
        db_table = 'tta_list'
        verbose_name = 'TTA List Detail'
        verbose_name_plural = 'TTA List Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  