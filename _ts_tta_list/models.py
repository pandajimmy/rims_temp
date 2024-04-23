from django.db import models
from django.db import connection

# Create your models here.
class TtaList_ts(models.Model):
    list_guid = models.CharField(primary_key=True, max_length=32)
    list_link_guid = models.CharField(max_length=32, blank=True, null=True)
    revision = models.CharField(max_length=100, blank=True, null=True)
    customer_guid = models.CharField(max_length=32)
    refno = models.CharField(max_length=20)
    supplier_guid = models.CharField(max_length=32)
    supplier_code = models.CharField(max_length=15, blank=True, null=True)
    supplier_name = models.CharField(max_length=60, blank=True, null=True)
    bill_supp_guid = models.CharField(max_length=32, blank=True, null=True)
    bill_supp_code = models.CharField(max_length=15, blank=True, null=True)
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True)
    negotiation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    co_reg_no = models.CharField(max_length=32, blank=True, null=True)
    tta_period_from = models.CharField(max_length=32, blank=True, null=True)
    tta_period_to = models.CharField(max_length=32, blank=True, null=True)
    internal_pic = models.CharField(max_length=60, blank=True, null=True)
    trading_group = models.CharField(max_length=60, blank=True, null=True)
    trading_type = models.CharField(max_length=60, blank=True, null=True)
    delivery_mode = models.CharField(max_length=60, blank=True, null=True)
    returnable = models.CharField(max_length=10, blank=True, null=True)
    supplier_pic = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_name = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_position = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_contact = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_email = models.CharField(max_length=60, blank=True, null=True)
    banner = models.TextField(blank=True, null=True)
    outlet = models.TextField(blank=True, null=True)
    supplier_profile = models.JSONField(blank=True, null=True)
    purchase_n_rebates = models.JSONField(blank=True, null=True)
    payment_n_discount = models.JSONField(blank=True, null=True)
    stock_n_deliveries = models.JSONField(blank=True, null=True)
    administration_fees = models.JSONField(blank=True, null=True)
    business_growth_support = models.JSONField(blank=True, null=True)
    promotion_support = models.JSONField(blank=True, null=True)
    display_incentive = models.JSONField(blank=True, null=True)
    marketing_support = models.JSONField(blank=True, null=True)
    e_commerce_support = models.JSONField(blank=True, null=True)
    concess_n_consign = models.JSONField(blank=True, null=True)
    data_sharing_plan = models.JSONField(blank=True, null=True)
    condition_of_trade = models.JSONField(blank=True, null=True)
    effective_date = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    submit_by = models.CharField(max_length=100, blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    approve_by = models.CharField(max_length=100, blank=True, null=True)
    reject_at = models.DateTimeField(blank=True, null=True)
    reject_by = models.CharField(max_length=100, blank=True, null=True)
    list_status = models.CharField(max_length=20, blank=True, null=True)
    ecommerce_support = models.JSONField(blank=True, null=True)
    purchase_rebate_tier = models.JSONField(blank=True, null=True)

    class Meta: 
        managed = False
        db_table = 'tta_list'
        ordering = ('refno','list_guid')
    

    def __str__(self):
        # cursor = connection.cursor()
        # cursor.execute("SET sort_buffer_size = 262144256000000")
        return self.refno

    def get_absolute_url(self):
        # cursor = connection.cursor()
        # cursor.execute("SET sort_buffer_size = 262144256000000")
        return f'/{self.refno}/'  

    def save():
        if self.list_link_guid == '':
	        self.list_link_guid = self.list_guid

        if self.list_link_guid == None:
            self.list_link_guid = self.list_guid
        
        if self.revision == '':
            self.revision = '0'

        super(TtaList_ts,self).save(*args, **kwargs)