import uuid
import hashlib
from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _ml_rims_brand.models import RimsBrand
from _mc_get_customer_profile.models import CustomerProfile

class TtaListTradingBrand(models.Model):
    list_brand_guid = models.CharField(primary_key=True, max_length=32, verbose_name='List Brand Guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='trading_brand')
    brand_guid = models.ForeignKey(RimsBrand, max_length=32, on_delete=models.DO_NOTHING, db_column='brand_guid', verbose_name='Brand guid', related_name='trading_brand_guid_list')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_trading_brand_customer_profile')

    class Meta:
        managed = False
        db_table = 'tta_list_brand'
        verbose_name = 'TTA List Trading Brand Detail'
        verbose_name_plural = 'TTA List Trading Brands Details'
        ordering = ('list_guid',)

    def __str__(self):
        return self.list_guid

    def get_absolute_url(self):
        return f'/{self.list_guid}/'

    def save(self, *args, **kwargs):
        # Ensure list_brand_guid is set
        if not self.list_brand_guid:
            self.list_brand_guid = self.generate_unique_guid()
        
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_guid():
        def random_guid_part():
            return hashlib.md5(uuid.uuid4().bytes).hexdigest()[:8].upper()
        return ''.join(random_guid_part() for _ in range(4))
