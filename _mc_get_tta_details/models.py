from django.db import models

class TtaList(models.Model):
    list_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    refno = models.CharField(max_length=20)
    supplier_guid = models.CharField(max_length=32)
    supplier_name = models.CharField(max_length=60, blank=True, null=True)
    bill_supp_guid = models.CharField(max_length=32)
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True)
    negotiation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    co_reg_no = models.IntegerField(blank=True, null=True)
    tta_period_from = models.CharField(max_length=200, blank=True, null=True)
    tta_period_to = models.CharField(max_length=200, blank=True, null=True)
    internal_pic = models.CharField(max_length=200, blank=True, null=True)
    trading_group = models.CharField(max_length=200, blank=True, null=True)
    trading_type = models.CharField(max_length=200, blank=True, null=True)
    delivery_mode = models.CharField(max_length=200, blank=True, null=True)
    returnable = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_name = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_position = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_contact = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_email = models.CharField(max_length=200, blank=True, null=True)
    banner = models.CharField(max_length=200, blank=True, null=True)
    outlet = models.CharField(max_length=200, blank=True, null=True)
    target_purchase_per_year_left_option = models.CharField(max_length=200, blank=True, null=True)
    target_purchase_per_year = models.IntegerField(blank=True, null=True)
    target_purchase_per_year_option = models.CharField(max_length=200, blank=True, null=True)
    flat_rebate_left_option = models.CharField(max_length=200, blank=True, null=True)
    flat_rebate = models.IntegerField(blank=True, null=True)
    flat_rebate_option = models.CharField(max_length=200, blank=True, null=True)
    business_development_fund_left_option = models.CharField(max_length=200, blank=True, null=True)
    business_development_fund = models.IntegerField(blank=True, null=True)
    business_development_fund_option = models.CharField(max_length=200, blank=True, null=True)
    payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True)
    payment_terms = models.CharField(max_length=200, blank=True, null=True)
    early_payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True)
    early_payment_terms = models.CharField(max_length=200, blank=True, null=True)
    early_payment_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    early_payment_discount = models.IntegerField(blank=True, null=True)
    early_payment_discount_option = models.CharField(max_length=200, blank=True, null=True)
    cross_docking_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    cross_docking_allowance = models.IntegerField(blank=True, null=True)
    cross_docking_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    east_malaysia_orders_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    east_malaysia_orders_allowance = models.IntegerField(blank=True, null=True)
    east_malaysia_orders_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    damage_good_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    damage_good_allowance = models.IntegerField(blank=True, null=True)
    damage_good_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    non_compliance_packaging_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    non_compliance_packaging_allowance = models.IntegerField(blank=True, null=True)
    non_compliance_packaging_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_fulfillment_left_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_fulfillment = models.IntegerField(blank=True, null=True)
    purchase_order_fulfillment_option = models.CharField(max_length=200, blank=True, null=True)
    unfulfilled_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    unfulfilled_penalty = models.IntegerField(blank=True, null=True)
    unfulfilled_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    lost_of_profit_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    lost_of_profit_penalty = models.IntegerField(blank=True, null=True)
    lost_of_profit_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time_left_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time_option = models.CharField(max_length=200, blank=True, null=True)
    lead_time_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    lead_time_penalty = models.IntegerField(blank=True, null=True)
    lead_time_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    account_administration_fee_left_option = models.CharField(max_length=200, blank=True, null=True)
    account_administration_fee = models.IntegerField(blank=True, null=True)
    account_administration_fee_option = models.CharField(max_length=200, blank=True, null=True)
    product_registration_fee_left_option = models.CharField(max_length=200, blank=True, null=True)
    product_registration_fee = models.IntegerField(blank=True, null=True)
    product_registration_fee_option = models.CharField(max_length=200, blank=True, null=True)
    sku_replacement_left_option = models.CharField(max_length=200, blank=True, null=True)
    sku_replacement = models.IntegerField(blank=True, null=True)
    sku_replacement_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_2 = models.IntegerField(blank=True, null=True)
    new_item_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_opening_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_opening = models.IntegerField(blank=True, null=True)
    new_store_opening_option = models.CharField(max_length=200, blank=True, null=True)
    refurbish_store_left_option = models.CharField(max_length=200, blank=True, null=True)
    refurbish_store = models.IntegerField(blank=True, null=True)
    refurbish_store_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_allowance = models.IntegerField(blank=True, null=True)
    anniversary_sales_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_orders_rebate_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_orders_rebate = models.IntegerField(blank=True, null=True)
    anniversary_orders_rebate_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_2 = models.IntegerField(blank=True, null=True)
    new_store_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales = models.IntegerField(blank=True, null=True)
    anniversary_sales_option = models.CharField(max_length=200, blank=True, null=True)
    chinese_new_year_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    chinese_new_year_sales = models.IntegerField(blank=True, null=True)
    chinese_new_year_sales_option = models.CharField(max_length=200, blank=True, null=True)
    hari_raya_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    hari_raya_sales = models.IntegerField(blank=True, null=True)
    hari_raya_sales_option = models.CharField(max_length=200, blank=True, null=True)
    christmas_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    christmas_sales = models.IntegerField(blank=True, null=True)
    christmas_sales_option = models.CharField(max_length=200, blank=True, null=True)
    in_store_display_left_option = models.CharField(max_length=200, blank=True, null=True)
    in_store_display = models.IntegerField(blank=True, null=True)
    in_store_display_option = models.CharField(max_length=200, blank=True, null=True)
    press_advertisement_n_mailer_left_option = models.CharField(max_length=200, blank=True, null=True)
    press_advertisement_n_mailer = models.IntegerField(blank=True, null=True)
    press_advertisement_n_mailer_option = models.CharField(max_length=200, blank=True, null=True)
    adhoc_support_left_option = models.CharField(max_length=200, blank=True, null=True)
    adhoc_support = models.IntegerField(blank=True, null=True)
    adhoc_support_option = models.CharField(max_length=200, blank=True, null=True)
    crm_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    crm_event = models.IntegerField(blank=True, null=True)
    crm_event_option = models.CharField(max_length=200, blank=True, null=True)
    marketing_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    marketing_event = models.IntegerField(blank=True, null=True)
    marketing_event_option = models.CharField(max_length=200, blank=True, null=True)
    concourse_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    concourse_event = models.IntegerField(blank=True, null=True)
    concourse_event_option = models.CharField(max_length=200, blank=True, null=True)
    system_setup_n_maintenance_left_option = models.CharField(max_length=200, blank=True, null=True)
    system_setup_n_maintenance = models.IntegerField(blank=True, null=True)
    system_setup_n_maintenance_option = models.CharField(max_length=200, blank=True, null=True)
    digital_communication_left_option = models.CharField(max_length=200, blank=True, null=True)
    digital_communication = models.IntegerField(blank=True, null=True)
    digital_communication_option = models.CharField(max_length=200, blank=True, null=True)
    social_media_post_left_option = models.CharField(max_length=200, blank=True, null=True)
    social_media_post = models.IntegerField(blank=True, null=True)
    social_media_post_option = models.CharField(max_length=200, blank=True, null=True)
    market_place_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    market_place_event = models.IntegerField(blank=True, null=True)
    market_place_event_option = models.CharField(max_length=200, blank=True, null=True)
    normal_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    normal_items = models.IntegerField(blank=True, null=True)
    normal_items_option = models.CharField(max_length=200, blank=True, null=True)
    best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    best_buy_items = models.IntegerField(blank=True, null=True)
    best_buy_items_option = models.CharField(max_length=200, blank=True, null=True)
    super_best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    super_best_buy_items = models.IntegerField(blank=True, null=True)
    super_best_buy_items_option = models.CharField(max_length=200, blank=True, null=True)
    mark_down_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    mark_down_items = models.IntegerField(blank=True, null=True)
    mark_down_items_option = models.CharField(max_length=200, blank=True, null=True)
    number_50_percent_discount_left_option = models.CharField(db_column='50_percent_discount_left_option', max_length=200, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50_percent_discount = models.IntegerField(db_column='50_percent_discount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50_percent_discount_option = models.CharField(db_column='50_percent_discount_option', max_length=200, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    data_sharing_subscription_left_option = models.CharField(max_length=200, blank=True, null=True)
    data_sharing_subscription = models.IntegerField(blank=True, null=True)
    data_sharing_subscription_option = models.CharField(max_length=200, blank=True, null=True)
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True)
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True)
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True)
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True)
    weekly_stock_listing_by_sku = models.CharField(max_length=200, blank=True, null=True)
    weekly_stock_listing_by_sku_option = models.CharField(max_length=200, blank=True, null=True)
    general_complicance = models.CharField(max_length=200, blank=True, null=True)
    return_condition = models.CharField(max_length=200, blank=True, null=True)
    price_n_billing = models.CharField(max_length=200, blank=True, null=True)
    effective_date = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    submit_by = models.CharField(max_length=20, blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    approve_by = models.CharField(max_length=20, blank=True, null=True)
    reject_at = models.DateTimeField(blank=True, null=True)
    reject_by = models.CharField(max_length=20, blank=True, null=True)
    list_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tta_list'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  