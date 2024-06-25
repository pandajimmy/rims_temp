from django.db import models
from _ts_tta_invmain.models import TtaInvmain
from _mc_get_customer_profile.models import CustomerProfile
from _lib import panda
from _lib import a_tta_cal
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
)

# Create your models here.
class TtaInvchild(models.Model):
    #customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_invchild_customer_profile')
    customer_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Customer guid')
    invchild_guid = models.CharField(primary_key=True, max_length=32, blank=True, verbose_name='Invoice Child guid')
    invmain_guid = models.ForeignKey(TtaInvmain, models.DO_NOTHING, db_column='invmain_guid', related_name='invchild_key', verbose_name='Invoice Main guid')
    line = models.IntegerField(blank=True, null=True, verbose_name='Line')
    pricetype = models.CharField(max_length=5, verbose_name='Price Type')
    itemcode = models.CharField(max_length=20, verbose_name='Item Code')
    description = models.CharField(max_length=50, verbose_name='Description')
    qty = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Quantity')
    unit_price = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Unit Price')
    #Previously calculated_val has not been declared in here
    calculated_val = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Calculated Val')
    disc1type = models.CharField(max_length=20, verbose_name='Discount 1 Type')
    disc1value = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Discount 1 Value')
    disc2type = models.CharField(max_length=20, verbose_name='Discount 2 Type')
    disc2value = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Discount 2 Value')
    totalprice = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Total Price')
    gst_tax_code = models.CharField(max_length=10, verbose_name='GST Tax Code')
    gst_tax_rate = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='GST Tax Rate')
    gst_tax_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='GST Tax Amount')
    total_incl_tax = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Total Including Tax')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'tta_invchild'
        ordering = ('invchild_guid',)

    def __str__(self):
        #return f'/{self.invchild_guid}/'  
        return self.invchild_guid

    def get_absolute_url(self):
        return f'/{self.invchild_guid}/'  

    def update_field(self, key, value):
    # This will raise an AttributeError if the key isn't an attribute 
    # of your model
        getattr(self, key) 
        setattr(self, key, value)


    def save(self, *args, **kwargs):    
        if self.invchild_guid == '':
            self.invchild_guid = panda.panda_uuid()        
            self.created_at = panda.panda_today()
            

            # allresult = McSysrun.objects.filter(prefix='TRIP').first()
            # new_refno = str(allresult.code) + str(allresult.year)[:2] + str(allresult.month).zfill(2) + str(allresult.day).zfill(2) + str(allresult.currentno).zfill(4)
            
            # self.refno = new_refno
            # t =  McSysrun.objects.get(prefix='TRIP')
            # t.currentno += 1  # change field
            # t.save() # this will update only

        if self.created_at == '' or self.created_at is None:
            self.created_at = panda.panda_today()

        
        
        self.updated_at=panda.panda_today()
        super(TtaInvchild,self).save(*args, **kwargs)

    

@receiver(pre_save, sender=TtaInvchild)
def pre_save_receiver(sender, instance, **kwargs):

    try:
        instance._pre_save_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        instance._pre_save_instance = None

@receiver(post_save, sender=TtaInvchild)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """     

    invmain = TtaInvchild.objects.filter(invchild_guid=instance.invchild_guid).values_list('invmain_guid', flat=True).first()
    
    a_tta_cal.update_header(invmain)