from django.db import models
from _lib import panda 
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.db import connection

from django.db.models.signals import (
    pre_save,
    post_save,
)
from django.dispatch import receiver



# Create your models here.
class TtaListCalMain(models.Model):
    cal_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    outlet = models.CharField(max_length=32)
    sup_code = models.CharField(max_length=20, blank=True, null=True)
    sup_name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    brand_desc = models.CharField(max_length=100, blank=True, null=True)
    gr_amt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    gr_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debitamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    creditamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    credit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    pdnamt = models.DecimalField(db_column='PDNamt', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pcnamt = models.DecimalField(db_column='PCNamt', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

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

        self.created_at=panda.panda_today()
        super(TtaListCalMain,self).save(*args, **kwargs)   
