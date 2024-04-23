from django.db import models
from _lib import panda

# Create your models here.
class DesignCot(models.Model):
    #cot_guid = models.CharField(primary_key=True, max_length=32)
    cot_guid = models.CharField(primary_key=True, max_length=32,default=panda.panda_uuid,editable=False)
    customer_guid = models.CharField(max_length=32)
    tab_guid = models.CharField(max_length=32)
    cot_group = models.CharField(max_length=120, blank=True, null=True)
    cot_seq = models.SmallIntegerField(blank=True, null=True)
    cot_description = models.CharField(max_length=120, blank=True, null=True)
    cot_value = models.TextField(blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    isdeleted = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_cot'
        unique_together = (('cot_guid', 'customer_guid', 'tab_guid'),)

    def __str__(self):
        return self.cot_guid

    def get_absolute_url(self):
        return f'/{self.cot_guid}/' 
    
