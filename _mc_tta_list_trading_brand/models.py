import uuid
import hashlib
from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _ml_rims_brand.models import RimsBrand

class TtaListTradingBrand(models.Model):
    list_brand_guid = models.CharField(primary_key=True, max_length=32, verbose_name='List Brand Guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='trading_brand_list')
    brand_guid = models.ForeignKey(RimsBrand, max_length=32, on_delete=models.DO_NOTHING, db_column='brand_guid', verbose_name='Brand guid', related_name='trading_brand_guid_list')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer guid')
    refno = models.CharField(max_length=20, editable=False, verbose_name='Reference No.')
    code = models.CharField(db_column='Code', max_length=10, blank=True, null=True, verbose_name='Code')

    class Meta:
        managed = False
        db_table = 'tta_list_brand'
        verbose_name = 'TTA List Trading Brand Detail'
        verbose_name_plural = 'TTA List Trading Brands Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'

    def save(self, *args, **kwargs):
        # Ensure list_brand_guid is set
        if not self.list_brand_guid:
            self.list_brand_guid = self.generate_unique_guid()
        
        # Set refno from related TtaList instance if not already set
        if not self.refno and self.list_guid:
            self.refno = self.list_guid.refno
        
        # Set code from related RimsBrand instance if not already set
        if not self.code and self.brand_guid:
            self.code = self.brand_guid.code
        
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_guid():
        def random_guid_part():
            return hashlib.md5(uuid.uuid4().bytes).hexdigest()[:8].upper()
        return ''.join(random_guid_part() for _ in range(4))
