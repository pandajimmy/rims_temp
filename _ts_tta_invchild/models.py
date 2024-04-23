from django.db import models
from _ts_tta_invmain.models import TtaInvmain
from _lib import panda
from _lib import a_tta_cal
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
)

# Create your models here.
class TtaInvchild(models.Model):
    customer_guid = models.CharField(max_length=32)
    invchild_guid = models.CharField(primary_key=True, max_length=32, blank=True)
    invmain_guid = models.ForeignKey(TtaInvmain, models.DO_NOTHING, db_column='invmain_guid', related_name='invchild_key') 
    line = models.IntegerField(blank=True, null=True)
    pricetype = models.CharField(max_length=5)
    itemcode = models.CharField(max_length=20)
    description = models.CharField(max_length=50 )
    qty = models.DecimalField(max_digits=14, decimal_places=2)
    unit_price = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    disc1type = models.CharField(max_length=20)
    disc1value = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    disc2type = models.CharField(max_length=20)
    disc2value = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    totalprice = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    gst_tax_code = models.CharField(max_length=10)
    gst_tax_rate = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    gst_tax_amount = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    total_incl_tax = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

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