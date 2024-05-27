from django.db import models
from _lib import panda
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class TtaCndnAmt(models.Model):
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_cndnamt_customer_profile')
    cndn_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Cndn guid')
    trans_type = models.CharField(max_length=10, blank=True, null=True, verbose_name='Transaction Type')
    loc_group = models.CharField(max_length=20, blank=True, null=True, verbose_name='Location Group')
    location = models.CharField(max_length=20, blank=True, null=True, verbose_name='Location')
    refno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Reference Number')
    docno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Document Number')
    docdate = models.DateField(blank=True, null=True, verbose_name='Document Date')
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Code')
    name = models.CharField(max_length=80, blank=True, null=True, verbose_name='Name')
    tax_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='Tax Code')
    remark = models.TextField(blank=True, null=True, verbose_name='Remark')
    term = models.CharField(max_length=10, blank=True, null=True, verbose_name='Term')
    amount = models.FloatField(blank=True, null=True, verbose_name='Amount')
    gst_tax_sum = models.FloatField(blank=True, null=True, verbose_name='GST Tax Sum')
    amount_include_tax = models.FloatField(blank=True, null=True, verbose_name='Amount Including Tax')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')
    posted = models.SmallIntegerField(blank=True, null=True, verbose_name='Posted')
    posted_at = models.DateTimeField(blank=True, null=True, verbose_name='Posted at')
    posted_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Posted by')
    sup_cn_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Supplier CN Number')
    sup_cn_date = models.DateField(blank=True, null=True, verbose_name='Supplier CN Date')
    doc_name_reg = models.CharField(max_length=80, blank=True, null=True, verbose_name='Document Name Register')
    gst_tax_rate = models.FloatField(blank=True, null=True, verbose_name='GST Tax Rate')
    multi_tax_code = models.SmallIntegerField(blank=True, null=True, verbose_name='Multi Tax Code')
    refno2 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Reference Number 2')
    gst_adj = models.FloatField(blank=True, null=True, verbose_name='GST Adjustment')
    rounding_adj = models.FloatField(blank=True, null=True, verbose_name='Rounding Adjustment')
    unpostby = models.CharField(max_length=80, blank=True, null=True, verbose_name='Unpost by')
    unpostdatetime = models.DateTimeField(blank=True, null=True, verbose_name='Unpost Date Time')
    subdeptcode = models.CharField(max_length=20, blank=True, null=True, verbose_name='Sub Department Code')
    export_account = models.CharField(max_length=10, blank=True, null=True, verbose_name='Export Account')
    export_at = models.DateTimeField(blank=True, null=True, verbose_name='Exported at')
    export_by = models.CharField(max_length=30, blank=True, null=True, verbose_name='Exported by')
    consign = models.SmallIntegerField(blank=True, null=True, verbose_name='Consign')
    hq_update = models.SmallIntegerField(blank=True, null=True, verbose_name='HQ Update')
    ibt = models.SmallIntegerField(blank=True, null=True, verbose_name='IBT')
    acc_posting_date = models.DateField(blank=True, null=True, verbose_name='Account Posting Date')
    trans_type_acc = models.CharField(max_length=10, blank=True, null=True, verbose_name='Transaction Type Account')
    doc_type = models.CharField(max_length=10, blank=True, null=True, verbose_name='Document Type')
    uploaded = models.SmallIntegerField(blank=True, null=True, verbose_name='Uploaded')
    uploaded_at = models.DateTimeField(blank=True, null=True, verbose_name='Uploaded at')
    cndn_doutlet_code = models.CharField(db_column='CNDN_DOutlet_code', max_length=20, blank=True, null=True, verbose_name='Cndn D Outlet Code')  # Field name made lowercase.
    cndn_salesman = models.CharField(db_column='CNDN_Salesman', max_length=30, blank=True, null=True, verbose_name='Cndn Salesman')  # Field name made lowercase.
    cndn_amtasdesc = models.CharField(db_column='CNDN_AmtAsDesc', max_length=200, blank=True, null=True, verbose_name='Cndn Amount As Description')  # Field name made lowercase.
    cndn_add1 = models.CharField(db_column='CNDN_Add1', max_length=60, blank=True, null=True, verbose_name='Cndn Address 1')  # Field name made lowercase.
    cndn_add2 = models.CharField(db_column='CNDN_Add2', max_length=60, blank=True, null=True, verbose_name='Cndn Address 2')  # Field name made lowercase.
    cndn_add3 = models.CharField(db_column='CNDN_Add3', max_length=60, blank=True, null=True, verbose_name='Cndn Address 3')  # Field name made lowercase.
    cndn_add4 = models.CharField(db_column='CNDN_Add4', max_length=60, blank=True, null=True, verbose_name='Cndn Address 4')  # Field name made lowercase.
    cndn_tel = models.CharField(db_column='CNDN_Tel', max_length=20, blank=True, null=True, verbose_name='Cndn Telephone')  # Field name made lowercase.
    cndn_fax = models.CharField(db_column='CNDN_Fax', max_length=20, blank=True, null=True, verbose_name='Cndn Fax')  # Field name made lowercase.
    cndn_dadd1 = models.CharField(db_column='CNDN_DAdd1', max_length=60, blank=True, null=True, verbose_name='Cndn Delivery Address 1')  # Field name made lowercase.
    cndn_dadd2 = models.CharField(db_column='CNDN_DAdd2', max_length=60, blank=True, null=True, verbose_name='Cndn Delivery Address 2')  # Field name made lowercase.
    cndn_dadd3 = models.CharField(db_column='CNDN_DAdd3', max_length=60, blank=True, null=True, verbose_name='Cndn Delivery Address 3')  # Field name made lowercase.
    cndn_dadd4 = models.CharField(db_column='CNDN_DAdd4', max_length=60, blank=True, null=True, verbose_name='Cndn Delivery Address 4')  # Field name made lowercase.
    cndn_dtel = models.CharField(db_column='CNDN_DTel', max_length=20, blank=True, null=True, verbose_name='Cndn Delivery Telephone')  # Field name made lowercase.
    cndn_dfax = models.CharField(db_column='CNDN_DFax', max_length=20, blank=True, null=True, verbose_name='Cndn Delivery Fax')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tta_cndn_amt'
        ordering = ('refno','cndn_guid')

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/' 
    
    
    def save(self, *args, **kwargs): 
        
        uuid = panda.panda_uuid()

        if self.cndn_guid =='':
            self.cndn_guid = uuid  
        
        self.updated_at=panda.panda_today()
        self.updated_by=self.updated_by
        super(TtaCndnAmt,self).save(*args, **kwargs)
