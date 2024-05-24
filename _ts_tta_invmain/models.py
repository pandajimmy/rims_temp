from django.db import models
from _lib import panda
from _mc_sysrun.models import Sysrun
from _mc_get_customer_profile.models import CustomerProfile
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
)
# Create your models here.
class TtaInvmain(models.Model):
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_invmain_customer_profile')
    invmain_guid = models.CharField(primary_key=True, max_length=32, blank=True, verbose_name='Invoice Main guid')
    refno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Reference Number')
    docno = models.CharField(max_length=25, blank=True, null=True, verbose_name='Document Number')
    invoice_date = models.DateField(blank=True, null=True, verbose_name='Invoice Date')
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Code')
    name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Name')
    add_1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Address Line 1')
    add_2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Address Line 2')
    add_3 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Address Line 3')
    add_4 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Address Line 4')
    attn = models.CharField(max_length=60, blank=True, null=True, verbose_name='Attn')
    term = models.CharField(max_length=20, blank=True, null=True, verbose_name='Term')
    remark = models.TextField(blank=True, null=True, verbose_name='Remark')
    subtotal1 = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Subtotal 1')
    discount1 = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Discount 1')
    discount1type = models.CharField(max_length=1, blank=True, null=True, verbose_name='Discount 1 Type')
    subtotal2 = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Subtotal 2')
    discount2 = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Discount 2')
    discount2type = models.CharField(max_length=1, blank=True, null=True, verbose_name='Discount 2 Type')
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Total')
    posted = models.IntegerField(blank=True, null=True, verbose_name='Posted')
    posted_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Posted by')
    posted_at = models.DateTimeField(blank=True, null=True, verbose_name='Posted at')
    export_account = models.CharField(max_length=32, blank=True, null=True, verbose_name='Export Account')
    export_at = models.DateTimeField(blank=True, null=True, verbose_name='Exported at')
    gst_tax_sum = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='GST Tax Sum')
    gst_tax_rate = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='GST Tax Rate')
    gst_adj = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='GST Adjustment')
    total_incl_tax = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Total Including Tax')
    doc_status = models.CharField(max_length=32, blank=True, null=True, verbose_name='Document Status')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated by')


    class Meta:
        managed = False
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
        super(TtaInvmain, self).save(*args, **kwargs)

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
