from django.db import models
from _mc_tta_list.models import TtaList  # Import your TtaList model
from _mc_get_customer_profile.models import CustomerProfile

class TtaListPromotionSupport(models.Model):
    # Main Details
    list_guid = models.OneToOneField(TtaList, primary_key=True,on_delete=models.DO_NOTHING,db_column='list_guid', verbose_name='List guid', related_name="promotion_support")
    list_link_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='List Link guid')
    promotion_guid = models.CharField(max_length=36, blank=True, null=False, editable=False, verbose_name='Promotion Support guid')
    revision = models.CharField(max_length=100, blank=True, null=True, verbose_name='Revision')
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='tta_promotion_support_customer_profile')
    refno = models.CharField(max_length=20,editable=False, verbose_name='Reference No.')

    # Middle Year Big Sales
    middle_year_big_sales_value = models.FloatField(blank=True, null=True, verbose_name='Middle Year Big Sales Value')
    middle_year_big_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Middle Year Big Sales Type')
    middle_year_big_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Middle Year Big Sales Value Type')
    middle_year_big_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Middle Year Big Sales Date To')
    middle_year_big_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Middle Year Big Sales Date From')
 
    # Top Brand
    top_brand_value = models.FloatField(blank=True, null=True, verbose_name='Top Brand Value')
    top_brand_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Top Brand Type')
    top_brand_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Top Brand Value Type')
    top_brand_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Top Brand Date To')
    top_brand_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Top Brand Date From')

    # Anniversary
    anniversary_value = models.FloatField(blank=True, null=True, verbose_name='Anniversary Value')
    anniversary_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Type')
    anniversary_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Value Type')
    anniversary_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Date To')
    anniversary_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Date From') 

    # Gawai
    gawai_value = models.FloatField(blank=True, null=True, verbose_name='Gawai Value')
    gawai_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Type')
    gawai_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Value Type')
    gawai_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Date To')
    gawai_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Date From')

    # Gawai Sales
    gawai_sales_value = models.FloatField(blank=True, null=True, verbose_name='Gawai Sales Value')
    gawai_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Sales Type')
    gawai_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Sales Value Type')
    gawai_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Sales Date To')
    gawai_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Gawai Sales Date From')

    # Anniversary Sales
    anniversary_sales_value = models.FloatField(blank=True, null=True, verbose_name='Anniversary Sales Value')
    anniversary_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Type')
    anniversary_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Value Type')
    anniversary_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Date To')
    anniversary_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Date From')

    # Chinese New Year Sales
    chinese_new_year_sales_value = models.FloatField(blank=True, null=True, verbose_name='Chinese New Year Sales Value')
    chinese_new_year_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Type')
    chinese_new_year_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Value Type')
    chinese_new_year_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Date To')
    chinese_new_year_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Date From')

    # Hari Raya Sales
    hari_raya_sales_value = models.FloatField(blank=True, null=True, verbose_name='Hari Raya Sales Value')
    hari_raya_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Type')
    hari_raya_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Value Type')
    hari_raya_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Date To')
    hari_raya_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Date From')

    # Christmas Sales
    christmas_sales_value = models.FloatField(blank=True, null=True, verbose_name='Christmas Sales Value')
    christmas_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Type')
    christmas_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Value Type')
    christmas_sales_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Date To')
    christmas_sales_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Date From')

    # Promotion Commission
    promotion_commission_value = models.FloatField(blank=True, null=True, verbose_name='Promotion Commission Value')
    promotion_commission_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Promotion Commission Type')
    promotion_commission_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Promotion Commission Value Type')
    promotion_commission_date_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='Promotion Commission Date To')
    promotion_commission_date_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='Promotion Commission Date From')

    # Details of Creation
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')
    
    class Meta:
        managed = False
        db_table = 'tta_list_promotionsupport'
        verbose_name = 'TTA List Promotion Support Detail'
        verbose_name_plural = 'TTA List Promotion Support Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  