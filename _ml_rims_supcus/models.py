from django.db import models

# Create your models here.
class RimsSupcus(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Customer Globally Unique Identifier')
    type = models.CharField(db_column='Type', max_length=1, verbose_name='Type')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=15, blank=True, null=True, verbose_name='Code')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True, verbose_name='Name')  # Field name made lowercase.
    add1 = models.CharField(db_column='Add1', max_length=60, blank=True, null=True, verbose_name='Address 1')  # Field name made lowercase.
    add2 = models.CharField(db_column='Add2', max_length=60, blank=True, null=True, verbose_name='Address 2')  # Field name made lowercase.
    add3 = models.CharField(db_column='Add3', max_length=60, blank=True, null=True, verbose_name='Address 3')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True, verbose_name='City')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True, verbose_name='State')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, blank=True, null=True, verbose_name='Country')  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=6, blank=True, null=True, verbose_name='Postcode')  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True, verbose_name='Telephone')  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True, verbose_name='Fax')  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=60, blank=True, null=True, verbose_name='Contact')  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=12, blank=True, null=True, verbose_name='Mobile')  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=30, blank=True, null=True, verbose_name='Term')  # Field name made lowercase.
    paymentday = models.IntegerField(db_column='PaymentDay', blank=True, null=True, verbose_name='Payment Day')  # Field name made lowercase.
    bankacc = models.CharField(db_column='BankAcc', max_length=35, blank=True, null=True, verbose_name='Bank Account')  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True, verbose_name='Credit Limit')  # Field name made lowercase.
    monitorcredit = models.SmallIntegerField(db_column='MonitorCredit', blank=True, null=True, verbose_name='Monitor Credit')  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True, verbose_name='Remark')  # Field name made lowercase.
    pointbf = models.FloatField(db_column='PointBF', blank=True, null=True, verbose_name='Point BF')  # Field name made lowercase.
    pointcumm = models.FloatField(db_column='PointCumm', blank=True, null=True, verbose_name='Point Cumulative')  # Field name made lowercase.
    pointsum = models.FloatField(db_column='PointSum', blank=True, null=True, verbose_name='Point Sum')  # Field name made lowercase.
    member = models.SmallIntegerField(db_column='Member', blank=True, null=True, verbose_name='Member')  # Field name made lowercase.
    memberno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Member Number')
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True, verbose_name='Expiry Date')  # Field name made lowercase.
    cyclevisit = models.IntegerField(db_column='CycleVisit', blank=True, null=True, verbose_name='Cycle Visit')  # Field name made lowercase.
    deliveryterm = models.IntegerField(blank=True, null=True, verbose_name='Delivery Term')
    issuedstamp = models.DateTimeField(db_column='IssuedStamp', blank=True, null=True, verbose_name='Issued Stamp')  # Field name made lowercase.
    laststamp = models.DateTimeField(db_column='LastStamp', blank=True, null=True, verbose_name='Last Stamp')  # Field name made lowercase.
    dadd1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Delivery Address 1')
    dadd2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Delivery Address 2')
    dadd3 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Delivery Address 3')
    dattn = models.CharField(max_length=60, blank=True, null=True, verbose_name='Attention')
    dtel = models.CharField(max_length=20, blank=True, null=True, verbose_name='Delivery Telephone')
    dfax = models.CharField(max_length=20, blank=True, null=True, verbose_name='Delivery Fax')
    email = models.CharField(max_length=60, blank=True, null=True, verbose_name='Email')
    accountcode = models.CharField(db_column='AccountCode', max_length=15, blank=True, null=True, verbose_name='Account Code')  # Field name made lowercase.
    accpdebit = models.CharField(db_column='AccPDebit', max_length=10, blank=True, null=True, verbose_name='Acc PDebit')  # Field name made lowercase.
    accpcredit = models.CharField(db_column='AccPCredit', max_length=10, blank=True, null=True, verbose_name='Acc PCredit')  # Field name made lowercase.
    calduedateby = models.CharField(db_column='CalDueDateby', max_length=30, blank=True, null=True, verbose_name='Cal Due Date by')  # Field name made lowercase.
    supcusgroup = models.CharField(db_column='supcusGroup', max_length=20, blank=True, null=True, verbose_name='Supcus Group')  # Field name made lowercase.
    region = models.CharField(max_length=10, blank=True, null=True, verbose_name='Region')
    pcode = models.CharField(max_length=10, blank=True, null=True, verbose_name='P Code')
    add4 = models.CharField(db_column='Add4', max_length=60, blank=True, null=True, verbose_name='Address 4')  # Field name made lowercase.
    contact2 = models.CharField(db_column='Contact2', max_length=60, blank=True, null=True, verbose_name='Contact 2')  # Field name made lowercase.
    dadd4 = models.CharField(db_column='DAdd4', max_length=60, blank=True, null=True, verbose_name='Delivery Address 4')  # Field name made lowercase.
    poprice_method = models.CharField(max_length=10, blank=True, null=True, verbose_name='PO Price Method')
    stockday_min = models.FloatField(blank=True, null=True, verbose_name='Stock Day Minimum')
    stockday_max = models.FloatField(blank=True, null=True, verbose_name='Stock Day Maximum')
    stock_returnable = models.FloatField(blank=True, null=True, verbose_name='Stock Returnable')
    stock_return_cost_type = models.CharField(max_length=10, blank=True, null=True, verbose_name='Stock Return Cost Type')
    autoclosepo = models.SmallIntegerField(db_column='AutoClosePO', blank=True, null=True, verbose_name='Auto Close PO')  # Field name made lowercase.
    consign = models.SmallIntegerField(db_column='Consign', blank=True, null=True, verbose_name='Consign')  # Field name made lowercase.
    block = models.SmallIntegerField(db_column='Block', blank=True, null=True, verbose_name='Block')  # Field name made lowercase.
    exclude_orderqty_control = models.SmallIntegerField(blank=True, null=True, verbose_name='Exclude Order Quantity Control')
    supcus_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Supcus Globally Unique Identifier')
    acc_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='Account No.')
    ord_w1 = models.SmallIntegerField(db_column='Ord_W1', blank=True, null=True, verbose_name='Ord W1')  # Field name made lowercase.
    ord_w2 = models.SmallIntegerField(db_column='Ord_W2', blank=True, null=True, verbose_name='Ord W2')  # Field name made lowercase.
    ord_w3 = models.SmallIntegerField(db_column='Ord_W3', blank=True, null=True, verbose_name='Ord W3')  # Field name made lowercase.
    ord_w4 = models.SmallIntegerField(db_column='Ord_W4', blank=True, null=True, verbose_name='Ord W4')  # Field name made lowercase.
    ord_d1 = models.SmallIntegerField(db_column='Ord_D1', blank=True, null=True, verbose_name='Ord D1')  # Field name made lowercase.
    ord_d2 = models.SmallIntegerField(db_column='Ord_D2', blank=True, null=True, verbose_name='Ord D2')  # Field name made lowercase.
    ord_d3 = models.SmallIntegerField(db_column='Ord_D3', blank=True, null=True, verbose_name='Ord D3')  # Field name made lowercase.
    ord_d4 = models.SmallIntegerField(db_column='Ord_D4', blank=True, null=True, verbose_name='Ord D4')  # Field name made lowercase.
    ord_d5 = models.SmallIntegerField(db_column='Ord_D5', blank=True, null=True, verbose_name='Ord D5')  # Field name made lowercase.
    ord_d6 = models.SmallIntegerField(db_column='Ord_D6', blank=True, null=True, verbose_name='Ord D6')  # Field name made lowercase.
    ord_d7 = models.SmallIntegerField(db_column='Ord_D7', blank=True, null=True, verbose_name='Ord D7')  # Field name made lowercase.
    rec_method_1 = models.SmallIntegerField(db_column='Rec_Method_1', blank=True, null=True, verbose_name='Rec Method 1')  # Field name made lowercase.
    rec_method_2 = models.SmallIntegerField(db_column='Rec_Method_2', blank=True, null=True, verbose_name='Rec Method 2')  # Field name made lowercase.
    rec_method_3 = models.SmallIntegerField(db_column='Rec_Method_3', blank=True, null=True, verbose_name='Rec Method 3')  # Field name made lowercase.
    rec_method_4 = models.SmallIntegerField(db_column='Rec_Method_4', blank=True, null=True, verbose_name='Rec Method 4')  # Field name made lowercase.
    rec_method_5 = models.SmallIntegerField(db_column='Rec_Method_5', blank=True, null=True, verbose_name='Rec Method 5')  # Field name made lowercase.
    pur_expiry_days = models.IntegerField(blank=True, null=True, verbose_name='Pur Expiry Dates')
    grn_baseon_pocost = models.SmallIntegerField(blank=True, null=True, verbose_name='Grn base on PO Cost')
    ord_set_global = models.SmallIntegerField(db_column='Ord_set_global', blank=True, null=True, verbose_name='Ord Set Global')  # Field name made lowercase.
    rules_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Rules Code')
    po_negative_qty = models.SmallIntegerField(blank=True, null=True, verbose_name='PO Negative Quantity')
    grpo_variance_qty = models.FloatField(blank=True, null=True, verbose_name='GrPO Variance Quantity')
    grpo_variance_price = models.FloatField(blank=True, null=True, verbose_name='GrPO Variance Price')
    price_include_tax = models.SmallIntegerField(blank=True, null=True, verbose_name='Price Include Tax')
    delivery_early_in_day = models.IntegerField(blank=True, null=True, verbose_name='Delivery Early in Day')
    delivery_late_in_day = models.IntegerField(blank=True, null=True, verbose_name='Delivery Late in Day')
    tax_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='Tax Code')
    gst_start_date = models.DateField(blank=True, null=True, verbose_name='GST Start Date')
    gst_no = models.CharField(max_length=15, blank=True, null=True, verbose_name='GST No.')
    reg_no = models.CharField(max_length=25, blank=True, null=True, verbose_name='Registration No.')
    name_reg = models.CharField(max_length=80, blank=True, null=True, verbose_name='Registration Name')
    multi_tax_rate = models.SmallIntegerField(blank=True, null=True, verbose_name='Multi Tax Rate')
    grn_allow_negative_margin = models.SmallIntegerField(blank=True, null=True, verbose_name='GRN Allow Negative Margin')
    rebate_as_inv = models.SmallIntegerField(blank=True, null=True, verbose_name='Rebate as Invoice')
    discount_as_inv = models.SmallIntegerField(blank=True, null=True, verbose_name='Discount as Invoice')
    poso_line_max = models.IntegerField(blank=True, null=True, verbose_name='POS Order Line Maximum')
    apply_actual_cn = models.SmallIntegerField(blank=True, null=True, verbose_name='Apply Actual CN')
    promorebateastaxinv = models.SmallIntegerField(db_column='PromoRebateAsTaxInv', blank=True, null=True, verbose_name='Promotion Rebate As Tax Invoice')  # Field name made lowercase.
    purchasednamtastaxinv = models.SmallIntegerField(db_column='PurchaseDNAmtAsTaxInv', blank=True, null=True, verbose_name='Purchase DNAmt As Tax Invoice')  # Field name made lowercase.
    member_accno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Member Account No.')
    roundingadjust = models.SmallIntegerField(db_column='RoundingAdjust', blank=True, null=True, verbose_name='Rounding Adjust')  # Field name made lowercase.
    mobile_po = models.SmallIntegerField(blank=True, null=True, verbose_name='Mobile PO')
    auto_grn_mobile_po = models.SmallIntegerField(blank=True, null=True, verbose_name='Auto Grn Mobile PO')
    min_expiry_day = models.SmallIntegerField(blank=True, null=True, verbose_name='Minimum Expiry Day')
    currency_code = models.CharField(max_length=5, blank=True, null=True, verbose_name='Currency Code')
    sstregno = models.CharField(db_column='SSTRegNo', max_length=20, blank=True, null=True, verbose_name='SST Registration Number')  # Field name made lowercase.
    ssteffectivedate = models.DateField(db_column='SSTEffectiveDate', blank=True, null=True, verbose_name='SST Effective Date')  # Field name made lowercase.
    sstdefaultcode = models.CharField(db_column='SSTDefaultCode', max_length=15, blank=True, null=True, verbose_name='SST Default Code')  # Field name made lowercase.
    sstdefaulttaxintno = models.IntegerField(db_column='SSTDefaultTaxIntNo', blank=True, null=True, verbose_name='SST Default Tax Int Number')  # Field name made lowercase.
    replenish_date = models.CharField(max_length=12, blank=True, null=True, verbose_name='Replenish Date')
    replenish_stockbalance = models.SmallIntegerField(blank=True, null=True, verbose_name='Replenish Stock Balance')
    b2b_registration = models.SmallIntegerField(blank=True, null=True, verbose_name='B2B Registration')
    cdi = models.SmallIntegerField(blank=True, null=True, verbose_name='CDI')
    cpm = models.SmallIntegerField(blank=True, null=True, verbose_name='CPM')
    auto_price_change = models.SmallIntegerField(blank=True, null=True, verbose_name='Auto Price Change')
    promo_date = models.SmallIntegerField(blank=True, null=True, verbose_name='Promotion Date')
    pos_sales = models.SmallIntegerField(blank=True, null=True, verbose_name='Point of Sale')
    sales_agent = models.CharField(max_length=30, blank=True, null=True, verbose_name='Sales Agent')
    stk_rtn_collect_day = models.SmallIntegerField(blank=True, null=True, verbose_name='Stock Return Collection Day')
    imported_at = models.DateTimeField(blank=True, null=True, verbose_name='Imported at')
    sync_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Sync Globally Unique Identifier')


    class Meta:
        managed = False
        db_table = 'rims_supcus'
        unique_together = (('customer_guid', 'code'),)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return f'/{self.code}/'  
