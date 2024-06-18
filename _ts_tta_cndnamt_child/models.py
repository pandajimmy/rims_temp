from django.db import models
from _ts_tta_cndnamt.models import TtaCndnAmt
from _mc_get_customer_profile.models import CustomerProfile
from _lib import panda
from datetime import datetime
import uuid

# Create your models here.
class TtaCndnAmtC(models.Model):
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_cndn_amt_child_customer_profile')
    cndn_child_guid = models.CharField(primary_key=True, max_length=32, editable=False, verbose_name='Child guid')
    cndn_guid = models.ForeignKey(TtaCndnAmt, models.DO_NOTHING, db_column='cndn_guid', related_name='cndn_guid_key', verbose_name='Cndn guid')
    seq = models.IntegerField(blank=True, null=True, verbose_name='Sequence')
    itemcode = models.CharField(max_length=20, blank=True, null=True, verbose_name='Item Code')
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True, verbose_name='Description')  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True, verbose_name='Quantity')  # Field name made lowercase.
    amount_c = models.FloatField(blank=True, null=True, verbose_name='Amount')
    gst_tax_type = models.CharField(max_length=5, blank=True, null=True, verbose_name='GST Tax Type')
    gst_tax_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='GST Tax Code')
    gst_tax_rate = models.FloatField(blank=True, null=True, verbose_name='GST Tax Rate')
    gst_tax_amount = models.FloatField(blank=True, null=True, verbose_name='GST Tax Amount')
    amount_c_include_tax = models.FloatField(blank=True, null=True, verbose_name='Amount Including Tax')
    remark = models.CharField(max_length=50, blank=True, null=True, verbose_name='Remark')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name='Updated by')
    dept = models.CharField(db_column='Dept', max_length=5, blank=True, null=True, verbose_name='Department')  # Field name made lowercase.
    subdept = models.CharField(db_column='SubDept', max_length=5, blank=True, null=True, verbose_name='Sub Department')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=5, blank=True, null=True, verbose_name='Category')  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=5, blank=True, null=True, verbose_name='Brand')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=5, blank=True, null=True, verbose_name='Manufacturer')  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=30, blank=True, null=True, verbose_name='Barcode')  # Field name made lowercase.
    reason = models.CharField(max_length=20, blank=True, null=True, verbose_name='Reason')
    itemtype = models.CharField(max_length=35, blank=True, null=True, verbose_name='Item Type')
    ori_inv_no = models.CharField(max_length=30, blank=True, null=True, verbose_name='Original Invoice Number')
    ori_inv_date = models.DateField(blank=True, null=True, verbose_name='Original Invoice Date')
    postdatetime_c = models.DateTimeField(blank=True, null=True, verbose_name='Posted Date Time')
    consign = models.SmallIntegerField(blank=True, null=True, verbose_name='Consign')
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True, verbose_name='Colour')  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, blank=True, null=True, verbose_name='Size')  # Field name made lowercase.
    articleno = models.CharField(db_column='ArticleNo', max_length=20, blank=True, null=True, verbose_name='Article Number')  # Field name made lowercase.
    packsize = models.FloatField(db_column='PackSize', blank=True, null=True, verbose_name='Pack Size')  # Field name made lowercase.
    um = models.CharField(db_column='UM', max_length=5, blank=True, null=True, verbose_name='Unit of Measurement')  # Field name made lowercase.
    itemlink = models.CharField(db_column='ItemLink', max_length=20, blank=True, null=True, verbose_name='Item Link')  # Field name made lowercase.
    hq_update = models.SmallIntegerField(blank=True, null=True, verbose_name='HQ Update')
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True, verbose_name='Unit Price')  # Field name made lowercase.
    byamt = models.SmallIntegerField(db_column='byAmt', blank=True, null=True, verbose_name='By Amount')  # Field name made lowercase.
    gst_manual = models.SmallIntegerField(blank=True, null=True, verbose_name='GST Manual')
    taxintno = models.IntegerField(db_column='TaxIntNo', blank=True, null=True, verbose_name='Tax Int Number')  # Field name made lowercase.
    taxcodemap = models.CharField(db_column='TaxCodeMap', max_length=15, blank=True, null=True, verbose_name='Tax Code Map')  # Field name made lowercase.
    taxvalue = models.FloatField(db_column='TaxValue', blank=True, null=True, verbose_name='Tax Value')  # Field name made lowercase.
    taxamount = models.FloatField(db_column='TaxAmount', blank=True, null=True, verbose_name='Tax Amount')  # Field name made lowercase.
    taxamountvariance = models.FloatField(db_column='TaxAmountVariance', blank=True, null=True, verbose_name='Tax Amount Variance')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tta_cndn_amt_c'
        ordering = ('cndn_child_guid','cndn_guid')

    def __str__(self):
        return self.child_guid

    def get_absolute_url(self):
        return f'/{self.cndn_child_guid}/' 
    
    def save(self, *args, **kwargs):
        uid = ''
        while not uid.startswith('CC'):
            uid = uuid.uuid4().hex.upper()

        if self.cndn_child_guid == '':
            self.cndn_child_guid = uid
            self.created_at = panda.panda_today()
            self.created_by = self.created_by  or "system"  # Default to 'system' if created_by is None
        
        self.updated_at = panda.panda_today()
        self.updated_by = self.updated_by  or "system"  # Default to 'system' if created_by is None

        super(TtaCndnAmtC, self).save(*args, **kwargs)
