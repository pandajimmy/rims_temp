from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model

class TtaListTradingBrand(models.Model):
    # Trading Brand Code
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='trading_brand_list')
    brand_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Brand guid')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer guid')
    
    class Meta:
        managed = False
        db_table = 'tta_list_tradingbrand'
        verbose_name = 'TTA List Trading Brand Detail'
        verbose_name_plural = 'TTA List Trading Brands Details'
        ordering = ('brand_guid',)

    def __str__(self):
        return self.brand_guid

    def get_absolute_url(self):
        return f'/{self.brand_guid}/'  