from django.db import models
from _lib import panda 
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.db import connection
from django.utils import timezone
from _mc_get_customer_profile.models import CustomerProfile

from django.db.models.signals import (
    pre_save,
    post_save,
)
from django.dispatch import receiver



# Create your models here.
class TtaListCalMain(models.Model):
    cal_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Cal guid')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='cal_main_customer_profile')
    docdate = models.DateField(blank=True, null=True, verbose_name='Document Date')
    outlet = models.CharField(max_length=32, verbose_name='Outlet')
    sup_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Supplier Code')
    sup_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Supplier Name')
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name='Brand')
    brand_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Brand Description')
    gr_amt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='GR Amount')
    gr_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='GR Surcharge')
    debitamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Debit Amount')
    debit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Debit Surcharge')
    creditamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Credit Amount')
    credit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='Credit Surcharge')
    pdnamt = models.DecimalField(db_column='PDNamt', max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='PDN Amount')  
    pcnamt = models.DecimalField(db_column='PCNamt', max_digits=16, decimal_places=2, blank=True, null=True, verbose_name='PCN Amount')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')

    class Meta:
        managed = False
        db_table = 'tta_list_cal_main' 
        ordering = ('cal_guid',)

    def __str__(self):
        return self.cal_guid

    def get_absolute_url(self):
        return f'/{self.cal_guid}/' 

    def save(self, *args, **kwargs):
        
        if self.cal_guid =='':
            self.cal_guid = panda.panda_uuid()  
            self.created_at = panda.panda_today()

        print("Cal Guid: ", self.cal_guid)
        print("Created At: ", self.created_at)
        super(TtaListCalMain,self).save(*args, **kwargs)  
