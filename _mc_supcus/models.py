from django.db import models

class Supcus(models.Model):
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    code = models.CharField(db_column='Code', primary_key=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add1 = models.CharField(db_column='Add1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add2 = models.CharField(db_column='Add2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add3 = models.CharField(db_column='Add3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=60, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymentday = models.IntegerField(db_column='PaymentDay', blank=True, null=True)  # Field name made lowercase.
    bankacc = models.CharField(db_column='BankAcc', max_length=35, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
    monitorcredit = models.SmallIntegerField(db_column='MonitorCredit', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    pointbf = models.FloatField(db_column='PointBF', blank=True, null=True)  # Field name made lowercase.
    pointcumm = models.FloatField(db_column='PointCumm', blank=True, null=True)  # Field name made lowercase.
    pointsum = models.FloatField(db_column='PointSum', blank=True, null=True)  # Field name made lowercase.
    member = models.SmallIntegerField(db_column='Member', blank=True, null=True)  # Field name made lowercase.
    memberno = models.CharField(max_length=20, blank=True, null=True)
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cyclevisit = models.IntegerField(db_column='CycleVisit', blank=True, null=True)  # Field name made lowercase.
    deliveryterm = models.IntegerField(db_column='DeliveryTerm', blank=True, null=True)  # Field name made lowercase.
    issuedstamp = models.DateTimeField(db_column='IssuedStamp', blank=True, null=True)  # Field name made lowercase.
    laststamp = models.DateTimeField(db_column='LastStamp', blank=True, null=True)  # Field name made lowercase.
    dadd1 = models.CharField(max_length=60, blank=True, null=True)
    dadd2 = models.CharField(max_length=60, blank=True, null=True)
    dadd3 = models.CharField(max_length=60, blank=True, null=True)
    dattn = models.CharField(max_length=60, blank=True, null=True)
    dtel = models.CharField(max_length=30, blank=True, null=True)
    dfax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    accountcode = models.CharField(db_column='AccountCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accpdebit = models.CharField(db_column='AccPDebit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accpcredit = models.CharField(db_column='AccPCredit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    calduedateby = models.CharField(db_column='CalDueDateby', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supcusgroup = models.CharField(db_column='supcusGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=10, blank=True, null=True)
    pcode = models.CharField(max_length=10, blank=True, null=True)
    add4 = models.CharField(db_column='Add4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    contact2 = models.CharField(db_column='Contact2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dadd4 = models.CharField(db_column='DAdd4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    poprice_method = models.CharField(max_length=10, blank=True, null=True)
    stockday_min = models.FloatField(blank=True, null=True)
    stockday_max = models.FloatField(blank=True, null=True)
    stock_returnable = models.FloatField(blank=True, null=True)
    stock_return_cost_type = models.CharField(max_length=10, blank=True, null=True)
    autoclosepo = models.SmallIntegerField(db_column='AutoClosePO', blank=True, null=True)  # Field name made lowercase.
    consign = models.SmallIntegerField(db_column='Consign', blank=True, null=True)  # Field name made lowercase.
    block = models.SmallIntegerField(db_column='Block', blank=True, null=True)  # Field name made lowercase.
    exclude_orderqty_control = models.SmallIntegerField(blank=True, null=True)
    supcus_guid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    acc_no = models.CharField(max_length=20, blank=True, null=True)
    ord_w1 = models.SmallIntegerField(db_column='Ord_W1', blank=True, null=True)  # Field name made lowercase.
    ord_w2 = models.SmallIntegerField(db_column='Ord_W2', blank=True, null=True)  # Field name made lowercase.
    ord_w3 = models.SmallIntegerField(db_column='Ord_W3', blank=True, null=True)  # Field name made lowercase.
    ord_w4 = models.SmallIntegerField(db_column='Ord_W4', blank=True, null=True)  # Field name made lowercase.
    ord_d1 = models.SmallIntegerField(db_column='Ord_D1', blank=True, null=True)  # Field name made lowercase.
    ord_d2 = models.SmallIntegerField(db_column='Ord_D2', blank=True, null=True)  # Field name made lowercase.
    ord_d3 = models.SmallIntegerField(db_column='Ord_D3', blank=True, null=True)  # Field name made lowercase.
    ord_d4 = models.SmallIntegerField(db_column='Ord_D4', blank=True, null=True)  # Field name made lowercase.
    ord_d5 = models.SmallIntegerField(db_column='Ord_D5', blank=True, null=True)  # Field name made lowercase.
    ord_d6 = models.SmallIntegerField(db_column='Ord_D6', blank=True, null=True)  # Field name made lowercase.
    ord_d7 = models.SmallIntegerField(db_column='Ord_D7', blank=True, null=True)  # Field name made lowercase.
    rec_method_1 = models.SmallIntegerField(db_column='Rec_Method_1', blank=True, null=True)  # Field name made lowercase.
    rec_method_2 = models.SmallIntegerField(db_column='Rec_Method_2', blank=True, null=True)  # Field name made lowercase.
    rec_method_3 = models.SmallIntegerField(db_column='Rec_Method_3', blank=True, null=True)  # Field name made lowercase.
    rec_method_4 = models.SmallIntegerField(db_column='Rec_Method_4', blank=True, null=True)  # Field name made lowercase.
    rec_method_5 = models.SmallIntegerField(db_column='Rec_Method_5', blank=True, null=True)  # Field name made lowercase.
    pur_expiry_days = models.IntegerField(blank=True, null=True)
    grn_baseon_pocost = models.SmallIntegerField(blank=True, null=True)
    ord_set_global = models.SmallIntegerField(db_column='Ord_set_global', blank=True, null=True)  # Field name made lowercase.
    rules_code = models.CharField(max_length=20, blank=True, null=True)
    po_negative_qty = models.SmallIntegerField(blank=True, null=True)
    grpo_variance_qty = models.FloatField(blank=True, null=True)
    grpo_variance_price = models.FloatField(blank=True, null=True)
    price_include_tax = models.SmallIntegerField(blank=True, null=True)
    delivery_early_in_day = models.IntegerField(blank=True, null=True)
    delivery_late_in_day = models.IntegerField(blank=True, null=True)
    tax_code = models.CharField(max_length=10, blank=True, null=True)
    gst_start_date = models.DateField(blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    reg_no = models.CharField(max_length=25, blank=True, null=True)
    name_reg = models.CharField(max_length=80, blank=True, null=True)
    multi_tax_rate = models.SmallIntegerField(blank=True, null=True)
    grn_allow_negative_margin = models.SmallIntegerField(blank=True, null=True)
    rebate_as_inv = models.SmallIntegerField(blank=True, null=True)
    discount_as_inv = models.SmallIntegerField(blank=True, null=True)
    poso_line_max = models.IntegerField(blank=True, null=True)
    apply_actual_cn = models.SmallIntegerField(blank=True, null=True)
    purchasednamtastaxinv = models.SmallIntegerField(db_column='PurchaseDNAmtAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    member_accno = models.CharField(max_length=20, blank=True, null=True)
    promorebateastaxinv = models.SmallIntegerField(db_column='PromoRebateAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    roundingadjust = models.SmallIntegerField(db_column='RoundingAdjust', blank=True, null=True)  # Field name made lowercase.
    mobile_po = models.SmallIntegerField(blank=True, null=True)
    auto_grn_mobile_po = models.SmallIntegerField(blank=True, null=True)
    min_expiry_day = models.SmallIntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=5, blank=True, null=True)
    sstregno = models.CharField(db_column='SSTRegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssteffectivedate = models.DateField(db_column='SSTEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    sstdefaultcode = models.CharField(db_column='SSTDefaultCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sstdefaulttaxintno = models.IntegerField(db_column='SSTDefaultTaxIntNo', blank=True, null=True)  # Field name made lowercase.
    replenish_date = models.CharField(max_length=12, blank=True, null=True)
    replenish_stockbalance = models.SmallIntegerField(blank=True, null=True)
    b2b_registration = models.SmallIntegerField(blank=True, null=True)
    cdi = models.SmallIntegerField(blank=True, null=True)
    cpm = models.SmallIntegerField(blank=True, null=True)
    auto_price_change = models.SmallIntegerField(blank=True, null=True)
    promo_date = models.SmallIntegerField(blank=True, null=True)
    pos_sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supcus'
        ordering = ('code',)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return f'/{self.code}/'  
