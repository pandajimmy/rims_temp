from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
)
# Create your models here.
class TtaInvmain(models.Model):
    customer_guid = models.CharField(max_length=32)
    invmain_guid = models.CharField(primary_key=True, max_length=32, blank=True)
    refno = models.CharField(max_length=20, blank=True, null=True)
    docno = models.CharField(max_length=25, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    add_1 = models.CharField(max_length=60, blank=True, null=True)
    add_2 = models.CharField(max_length=60, blank=True, null=True)
    add_3 = models.CharField(max_length=60, blank=True, null=True)
    add_4 = models.CharField(max_length=60, blank=True, null=True)
    attn = models.CharField(max_length=60, blank=True, null=True)
    term = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    subtotal1 = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    discount1 = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    discount1type = models.CharField(max_length=1, blank=True, null=True)
    subtotal2 = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    discount2 = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    discount2type = models.CharField(max_length=1, blank=True, null=True)
    total = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    posted = models.IntegerField(blank=True, null=True)
    posted_by = models.CharField(max_length=32, blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    export_account = models.CharField(max_length=32, blank=True, null=True)
    export_at = models.DateTimeField(blank=True, null=True)
    gst_tax_sum = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    gst_tax_rate = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    gst_adj = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    total_incl_tax = models.DecimalField(max_digits=14, decimal_places=2,default=0.00)
    doc_status = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tta_invmain'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  
    
    def save(self, *args, **kwargs):    
        if self.invmain_guid == '':
            self.invmain_guid = panda.panda_uuid()        
            self.created_at = panda.panda_today() 

        if self.created_at == '' or self.created_at is None:
            self.created_at = panda.panda_today()

        module_type = 'INV'
        allresult = Sysrun.objects.filter(customer_guid=self.customer_guid, type=module_type).first()  

        new_refno = str(allresult.customer_prefix) + str(allresult.type) + str(allresult.yyyy)[-2:] + str(allresult.mm).zfill(2) + str(allresult.currentno).zfill(4)
        # print(self.refno)

        if (self.refno == '') or (self.refno == None)  :
            self.refno = new_refno 
            t =  Sysrun.objects.get(customer_guid=self.customer_guid, type=module_type)  
            t.currentno += 1  # change field
            t.save() # this will update only
        
        self.updated_at=panda.panda_today()
        self.doc_status=0
        self.posted=0
        super(TtaInvmain,self).save(*args, **kwargs) 

@receiver(pre_save, sender=TtaInvmain)
def pre_save_receiver(sender, instance, **kwargs):

    try:
        instance._pre_save_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        instance._pre_save_instance = None

@receiver(post_save, sender=TtaInvmain)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database
    """
    # if instance._pre_save_instance is not None:
    #     panda.log_general(instance._pre_save_instance, instance, 'ts_trip_do', instance.updated_by) 
    # invmain = TtaInvmain.objects.filter(invmain_guid=instance.invmain_guid).values_list('refno', flat=True).first()
    
    # a_tta_cal.update_header(invmain)
