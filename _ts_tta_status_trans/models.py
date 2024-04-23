from django.db import models
from _lib import panda

# Create your models here.
class TtaListStatusTrans(models.Model):
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    list_guid = models.CharField(max_length=32, blank=True, null=True)
    trans_guid = models.CharField(primary_key=True, max_length=32,editable=False)
    status_key = models.CharField(max_length=30, blank=True, null=True)
    status_description = models.CharField(max_length=32, blank=True, null=True)
    status_process = models.CharField(max_length=60, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tta_list_status_trans'
        
    def save(self, *args, **kwargs):
        print(self.customer_guid)
        
        if self.trans_guid =='':
	        self.trans_guid = panda.panda_uuid()  

        self.created_at=panda.panda_today()
        self.updated_at=panda.panda_today()
        self.updated_by=self.updated_by
        super(TtaListStatusTrans,self).save(*args, **kwargs)