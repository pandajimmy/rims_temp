from django.db import models

# Create your models here.
class RimsDivDeptSdC(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    trans_guid = models.CharField(max_length=32)
    group_code = models.CharField(max_length=120, blank=True, null=True)
    group_desc = models.CharField(max_length=120, blank=True, null=True)
    dept = models.CharField(max_length=120, blank=True, null=True)
    dept_desc = models.CharField(max_length=120, blank=True, null=True)
    subdept = models.CharField(max_length=120, blank=True, null=True)
    subdeptdesc = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null=True)
    category_desc = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rims_div_dept_sd_c'
        unique_together = (('customer_guid', 'trans_guid'),)
        ordering = ('customer_guid','trans_guid')

    def __str__(self):
        return self.trans_guid

    def get_absolute_url(self):
        return f'/{self.trans_guid}/' 

    