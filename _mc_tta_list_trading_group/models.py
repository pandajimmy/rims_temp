import uuid
import hashlib
from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _ml_rims_div_dept_sd_c.models import RimsDivDeptSdC
from _mc_get_customer_profile.models import CustomerProfile

class TtaListTradingGroup(models.Model):
    list_group_guid = models.CharField(primary_key=True, max_length=32, verbose_name='List Group Guid')
    list_guid = models.ForeignKey(TtaList, on_delete=models.DO_NOTHING, db_column='list_guid', verbose_name='List guid', related_name='trading_group')
    group_code = models.CharField(max_length=32, verbose_name='Group Code')
    trans_guid = models.ForeignKey(RimsDivDeptSdC, max_length=32, on_delete=models.DO_NOTHING, db_column='trans_guid', verbose_name='Brand guid', related_name='trading_group_code_list')
    customer_guid = models.ForeignKey(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_trading_group_customer_profile')

    class Meta:
        managed = False
        db_table = 'tta_list_tradinggroup'
        verbose_name = 'TTA List Trading Group Detail'
        verbose_name_plural = 'TTA List Trading Group Details'
        ordering = ('list_guid',)

    def __str__(self):
        return self.list_guid

    def get_absolute_url(self):
        return f'/{self.list_guid}/'

    def save(self, *args, **kwargs):
        # Ensure list_group_guid is set
        if not self.list_group_guid:
            self.list_group_guid = self.generate_unique_guid()
        
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_guid():
        def random_guid_part():
            return hashlib.md5(uuid.uuid4().bytes).hexdigest()[:8].upper()
        return ''.join(random_guid_part() for _ in range(4))
