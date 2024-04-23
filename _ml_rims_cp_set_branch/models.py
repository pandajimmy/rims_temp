from django.db import models

# Create your models here.
class RimsCpSetBranch(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    branch_guid = models.CharField(db_column='BRANCH_GUID', max_length=32)  # Field name made lowercase.
    branch_code = models.CharField(db_column='BRANCH_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='BRANCH_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    branch_add = models.TextField(db_column='BRANCH_ADD', blank=True, null=True)  # Field name made lowercase.
    branch_tel = models.CharField(db_column='BRANCH_TEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branch_fax = models.CharField(db_column='BRANCH_FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    script_tablename = models.CharField(db_column='SCRIPT_TABLENAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set_ratio = models.FloatField(db_column='SET_RATIO', blank=True, null=True)  # Field name made lowercase.
    set_priority = models.IntegerField(db_column='SET_PRIORITY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set_supplier_code = models.CharField(db_column='SET_SUPPLIER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set_customer_code = models.CharField(db_column='SET_CUSTOMER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sshhostname = models.CharField(db_column='sshHostname', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sshport = models.IntegerField(db_column='sshPort', blank=True, null=True)  # Field name made lowercase.
    sshuser = models.CharField(db_column='sshUser', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sshpass = models.CharField(db_column='sshPass', max_length=30, blank=True, null=True)  # Field name made lowercase.
    databaset_default = models.CharField(max_length=50, blank=True, null=True)
    mysql_user = models.CharField(max_length=30, blank=True, null=True)
    mysql_pass = models.CharField(max_length=30, blank=True, null=True)
    sshcdesthost = models.CharField(db_column='sshCDestHost', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sshcdestport = models.IntegerField(db_column='sshCDestPort', blank=True, null=True)  # Field name made lowercase.
    sshcsourceport = models.IntegerField(db_column='sshCSourcePort', blank=True, null=True)  # Field name made lowercase.
    script_database_tablename = models.CharField(max_length=40, blank=True, null=True)
    outlet_code_acc = models.CharField(db_column='OUTLET_CODE_ACC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    periodendon = models.IntegerField(db_column='PeriodEndOn', blank=True, null=True)  # Field name made lowercase.
    lastrecaldatetime = models.DateTimeField(db_column='LastRecalDateTime', blank=True, null=True)  # Field name made lowercase.
    recaltime = models.TimeField(db_column='RecalTime', blank=True, null=True)  # Field name made lowercase.
    nontrade_as_stock = models.SmallIntegerField(blank=True, null=True)
    set_active = models.SmallIntegerField(blank=True, null=True)
    is_dc = models.SmallIntegerField(blank=True, null=True)
    rep_all_ads = models.SmallIntegerField(blank=True, null=True)
    branch_desc = models.CharField(max_length=20, blank=True, null=True)
    fifo_calc = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rims_cp_set_branch'
        unique_together = (('customer_guid', 'branch_guid'),)
        ordering = ('customer_guid','branch_code')

    def __str__(self):
        return self.branch_guid

    def get_absolute_url(self):
        return f'/{self.branch_guid}/' 