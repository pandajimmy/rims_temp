from django.db import models

# Create your models here.
class RimsDivDeptSdC(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Customer Globally Unique Identifier')
    trans_guid = models.CharField(max_length=32, verbose_name='Transaction Globally Unique Identifier')
    group_code = models.CharField(max_length=120, blank=True, null=True, verbose_name='Group Code')
    group_desc = models.CharField(max_length=120, blank=True, null=True, verbose_name='Group Description')
    dept = models.CharField(max_length=120, blank=True, null=True, verbose_name='Department')
    dept_desc = models.CharField(max_length=120, blank=True, null=True, verbose_name='Department Description')
    subdept = models.CharField(max_length=120, blank=True, null=True, verbose_name='Subdepartment')
    subdeptdesc = models.CharField(max_length=120, blank=True, null=True, verbose_name='Subdepartment Description')
    category = models.CharField(max_length=120, blank=True, null=True, verbose_name='Category')
    category_desc = models.CharField(max_length=120, blank=True, null=True, verbose_name='Category Description')

    class Meta:
        managed = False
        db_table = 'rims_div_dept_sd_c'
        unique_together = (('customer_guid', 'trans_guid'),)
        ordering = ('customer_guid','trans_guid')

    def __str__(self):
        return self.trans_guid

    def get_absolute_url(self):
        return f'/{self.trans_guid}/' 

    