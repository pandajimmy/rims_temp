from django.db import models
from _ts_tta_cndnamt.models import TtaCndnAmt

# Create your models here.
class TtaCndnAmtC(models.Model):
    customer_guid = models.CharField(max_length=32)
    child_guid = models.CharField(primary_key=True, max_length=32)
    cndn_guid = models.ForeignKey(TtaCndnAmt, models.DO_NOTHING, db_column='cndn_guid', related_name = 'cndn_guid_key')
    seq = models.IntegerField(blank=True, null=True)
    itemcode = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    amount_c = models.FloatField(blank=True, null=True)
    gst_tax_type = models.CharField(max_length=5, blank=True, null=True)
    gst_tax_code = models.CharField(max_length=10, blank=True, null=True)
    gst_tax_rate = models.FloatField(blank=True, null=True)
    gst_tax_amount = models.FloatField(blank=True, null=True)
    amount_c_include_tax = models.FloatField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    dept = models.CharField(db_column='Dept', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subdept = models.CharField(db_column='SubDept', max_length=5, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=5, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=5, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=5, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=20, blank=True, null=True)
    itemtype = models.CharField(max_length=35, blank=True, null=True)
    ori_inv_no = models.CharField(max_length=30, blank=True, null=True)
    ori_inv_date = models.DateField(blank=True, null=True)
    postdatetime_c = models.DateTimeField(blank=True, null=True)
    consign = models.SmallIntegerField(blank=True, null=True)
    colour = models.CharField(db_column='Colour', max_length=20, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=20, blank=True, null=True)  # Field name made lowercase.
    articleno = models.CharField(db_column='ArticleNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packsize = models.FloatField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    um = models.CharField(db_column='UM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    itemlink = models.CharField(db_column='ItemLink', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hq_update = models.SmallIntegerField(blank=True, null=True)
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    byamt = models.SmallIntegerField(db_column='byAmt', blank=True, null=True)  # Field name made lowercase.
    gst_manual = models.SmallIntegerField(blank=True, null=True)
    taxintno = models.IntegerField(db_column='TaxIntNo', blank=True, null=True)  # Field name made lowercase.
    taxcodemap = models.CharField(db_column='TaxCodeMap', max_length=15, blank=True, null=True)  # Field name made lowercase.
    taxvalue = models.FloatField(db_column='TaxValue', blank=True, null=True)  # Field name made lowercase.
    taxamount = models.FloatField(db_column='TaxAmount', blank=True, null=True)  # Field name made lowercase.
    taxamountvariance = models.FloatField(db_column='TaxAmountVariance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tta_cndn_amt_c'
        ordering = ('child_guid','cndn_guid')

    def __str__(self):
        return self.child_guid

    def get_absolute_url(self):
        return f'/{self.child_guid}/' 