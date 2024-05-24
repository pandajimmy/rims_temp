from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

# Create your models here.
class RimsCpSetBranch(models.Model):
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='rims_cp_set_branch_customer_profile')
    branch_guid = models.CharField(primary_key=True, db_column='BRANCH_GUID', max_length=32, verbose_name='Branch guid')
    branch_code = models.CharField(db_column='BRANCH_CODE', max_length=20, blank=True, null=True, verbose_name='Branch Code')
    branch_name = models.CharField(db_column='BRANCH_NAME', max_length=60, blank=True, null=True, verbose_name='Branch Name')
    branch_add = models.TextField(db_column='BRANCH_ADD', blank=True, null=True, verbose_name='Branch Address')
    branch_tel = models.CharField(db_column='BRANCH_TEL', max_length=30, blank=True, null=True, verbose_name='Branch Telephone')
    branch_fax = models.CharField(db_column='BRANCH_FAX', max_length=30, blank=True, null=True, verbose_name='Branch Fax')
    script_tablename = models.CharField(db_column='SCRIPT_TABLENAME', max_length=20, blank=True, null=True, verbose_name='Script Table Name')
    set_ratio = models.FloatField(db_column='SET_RATIO', blank=True, null=True, verbose_name='Set Ratio')
    set_priority = models.IntegerField(db_column='SET_PRIORITY', blank=True, null=True, verbose_name='Set Priority')
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(db_column='CREATED_BY', max_length=30, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=30, blank=True, null=True, verbose_name='Updated By')
    set_supplier_code = models.CharField(db_column='SET_SUPPLIER_CODE', max_length=20, blank=True, null=True, verbose_name='Set Supplier Code')
    set_customer_code = models.CharField(db_column='SET_CUSTOMER_CODE', max_length=20, blank=True, null=True, verbose_name='Set Customer Code')
    sshhostname = models.CharField(db_column='sshHostname', max_length=60, blank=True, null=True, verbose_name='SSH Hostname')
    sshport = models.IntegerField(db_column='sshPort', blank=True, null=True, verbose_name='SSH Port')
    sshuser = models.CharField(db_column='sshUser', max_length=30, blank=True, null=True, verbose_name='SSH User')
    sshpass = models.CharField(db_column='sshPass', max_length=30, blank=True, null=True, verbose_name='SSH Password')
    databaset_default = models.CharField(max_length=50, blank=True, null=True, verbose_name='Default Database')
    mysql_user = models.CharField(max_length=30, blank=True, null=True, verbose_name='MySQL User')
    mysql_pass = models.CharField(max_length=30, blank=True, null=True, verbose_name='MySQL Password')
    sshcdesthost = models.CharField(db_column='sshCDestHost', max_length=50, blank=True, null=True, verbose_name='SSH CDest Host')
    sshcdestport = models.IntegerField(db_column='sshCDestPort', blank=True, null=True, verbose_name='SSH CDest Port')
    sshcsourceport = models.IntegerField(db_column='sshCSourcePort', blank=True, null=True, verbose_name='SSH CSource Port')
    script_database_tablename = models.CharField(max_length=40, blank=True, null=True, verbose_name='Script Database Table Name')
    outlet_code_acc = models.CharField(db_column='OUTLET_CODE_ACC', max_length=20, blank=True, null=True, verbose_name='Outlet Code ACC')
    periodendon = models.IntegerField(db_column='PeriodEndOn', blank=True, null=True, verbose_name='Period End On')
    lastrecaldatetime = models.DateTimeField(db_column='LastRecalDateTime', blank=True, null=True, verbose_name='Last Recalculation Datetime')
    recaltime = models.TimeField(db_column='RecalTime', blank=True, null=True, verbose_name='Recalculation Time')
    nontrade_as_stock = models.SmallIntegerField(blank=True, null=True, verbose_name='Non-Trade as Stock')
    set_active = models.SmallIntegerField(blank=True, null=True, verbose_name='Set Active')
    is_dc = models.SmallIntegerField(blank=True, null=True, verbose_name='Is DC')
    rep_all_ads = models.SmallIntegerField(blank=True, null=True, verbose_name='Rep All Ads')
    branch_desc = models.CharField(max_length=20, blank=True, null=True, verbose_name='Branch Description')
    fifo_calc = models.SmallIntegerField(blank=True, null=True, verbose_name='FIFO Calculation')

    class Meta:
        managed = False
        db_table = 'rims_cp_set_branch'
        unique_together = (('customer_guid', 'branch_guid'),)
        ordering = ('customer_guid','branch_code')

    def __str__(self):
        return self.branch_guid

    def get_absolute_url(self):
        return f'/{self.branch_guid}/' 