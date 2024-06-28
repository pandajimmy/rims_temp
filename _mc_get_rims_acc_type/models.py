from django.db import models
from _lib import panda

class RimsAccType(models.Model):
    # Main Details
    acc_type_guid = models.CharField(primary_key=True, max_length=32, editable=False, verbose_name='Acc Type guid')
    acc_type_code = models.CharField(max_length=20, verbose_name='Acc Type Code')
    acc_type_description = models.CharField(max_length=60, verbose_name='Acc Type Description')
    isactive = models.SmallIntegerField(verbose_name="Is Active")
    					
    class Meta:
        managed = False
        db_table = 'rims_acc_type'
        verbose_name = 'Rims Acc Type'
        verbose_name_plural = 'Rims Acc Types'
        ordering = ('acc_type_code',)

    def __str__(self):
        return self.acc_type_code

    def get_absolute_url(self):
        return f'/{self.acc_type_code}/'  
    
    def save(self, *args, **kwargs):

        # Generate a new UUID
        if not self.acc_type_guid:  
            self.acc_type_guid = panda.panda_uuid()

        super(RimsAccType, self).save(*args, **kwargs)