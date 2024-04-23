from django.db import models
from _lib import panda

# Create your models here.
class TtaCndnAmt(models.Model):
    customer_guid = models.CharField(max_length=32)
    cndn_guid = models.CharField(primary_key=True, max_length=32)
    trans_type = models.CharField(max_length=10, blank=True, null=True)
    loc_group = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    refno = models.CharField(max_length=20, blank=True, null=True)
    docno = models.CharField(max_length=20, blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    tax_code = models.CharField(max_length=10, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    term = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    gst_tax_sum = models.FloatField(blank=True, null=True)
    amount_include_tax = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    posted = models.SmallIntegerField(blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=20, blank=True, null=True)
    sup_cn_no = models.CharField(max_length=20, blank=True, null=True)
    sup_cn_date = models.DateField(blank=True, null=True)
    doc_name_reg = models.CharField(max_length=80, blank=True, null=True)
    gst_tax_rate = models.FloatField(blank=True, null=True)
    multi_tax_code = models.SmallIntegerField(blank=True, null=True)
    refno2 = models.CharField(max_length=20, blank=True, null=True)
    gst_adj = models.FloatField(blank=True, null=True)
    rounding_adj = models.FloatField(blank=True, null=True)
    unpostby = models.CharField(max_length=80, blank=True, null=True)
    unpostdatetime = models.DateTimeField(blank=True, null=True)
    subdeptcode = models.CharField(max_length=20, blank=True, null=True)
    export_account = models.CharField(max_length=10, blank=True, null=True)
    export_at = models.DateTimeField(blank=True, null=True)
    export_by = models.CharField(max_length=30, blank=True, null=True)
    consign = models.SmallIntegerField(blank=True, null=True)
    hq_update = models.SmallIntegerField(blank=True, null=True)
    ibt = models.SmallIntegerField(blank=True, null=True)
    acc_posting_date = models.DateField(blank=True, null=True)
    trans_type_acc = models.CharField(max_length=10, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    uploaded = models.SmallIntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)
    cndn_doutlet_code = models.CharField(db_column='CNDN_DOutlet_code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cndn_salesman = models.CharField(db_column='CNDN_Salesman', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cndn_amtasdesc = models.CharField(db_column='CNDN_AmtAsDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cndn_add1 = models.CharField(db_column='CNDN_Add1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_add2 = models.CharField(db_column='CNDN_Add2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_add3 = models.CharField(db_column='CNDN_Add3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_add4 = models.CharField(db_column='CNDN_Add4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_tel = models.CharField(db_column='CNDN_Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cndn_fax = models.CharField(db_column='CNDN_Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cndn_dadd1 = models.CharField(db_column='CNDN_DAdd1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_dadd2 = models.CharField(db_column='CNDN_DAdd2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_dadd3 = models.CharField(db_column='CNDN_DAdd3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_dadd4 = models.CharField(db_column='CNDN_DAdd4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cndn_dtel = models.CharField(db_column='CNDN_DTel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cndn_dfax = models.CharField(db_column='CNDN_DFax', max_length=20, blank=True, null=True)  # Field name made lowercase.

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
