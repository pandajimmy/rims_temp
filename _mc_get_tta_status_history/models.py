from django.db import models

class TtaList(models.Model):
    list_guid = models.CharField(primary_key=True, max_length=32, verbose_name="List Globally Unique Identifier")
    customer_guid = models.CharField(max_length=32, verbose_name="Customer Globally Unique Identifier")
    refno = models.CharField(max_length=20, verbose_name="Reference Number")
    supplier_guid = models.CharField(max_length=32, verbose_name="Supplier Globally Unique Identifier")
    supplier_name = models.CharField(max_length=60, blank=True, null=True, verbose_name="Supplier Name")
    bill_supp_guid = models.CharField(max_length=32, verbose_name="Billing Supplier Globally Unique Identifier")
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True, verbose_name="Billing Supplier Name")
    negotiation_year = models.TextField(blank=True, null=True, verbose_name="Negotiation Year")
    co_reg_no = models.IntegerField(blank=True, null=True, verbose_name="Company Registration Number")
    tta_period_from = models.CharField(max_length=200, blank=True, null=True, verbose_name="TTA Period From")
    tta_period_to = models.CharField(max_length=200, blank=True, null=True, verbose_name="TTA Period To")
    internal_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name="Internal PIC")
    trading_group = models.CharField(max_length=200, blank=True, null=True, verbose_name="Trading Group")
    trading_type = models.CharField(max_length=200, blank=True, null=True, verbose_name="Trading Type")
    delivery_mode = models.CharField(max_length=200, blank=True, null=True, verbose_name="Delivery Mode")
    returnable = models.CharField(max_length=200, blank=True, null=True, verbose_name="Returnable")
    supplier_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name="Supplier PIC")
    supplier_pic_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Supplier PIC Name")
    supplier_pic_position = models.CharField(max_length=200, blank=True, null=True, verbose_name="Supplier PIC Position")
    supplier_pic_contact = models.CharField(max_length=200, blank=True, null=True, verbose_name="Supplier PIC Contact")
    supplier_pic_email = models.CharField(max_length=200, blank=True, null=True, verbose_name="Supplier PIC Email")
    banner = models.CharField(max_length=200, blank=True, null=True, verbose_name="Banner")
    outlet = models.CharField(max_length=200, blank=True, null=True, verbose_name="Outlet")
    target_purchase_per_year_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Target Purchase per Year Left Option")
    target_purchase_per_year = models.IntegerField(blank=True, null=True, verbose_name="Target Purchase per Year")
    target_purchase_per_year_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Target Purchase per Year Option")
    flat_rebate_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Flat Rebate Left Option")
    flat_rebate = models.IntegerField(blank=True, null=True, verbose_name="Flat Rebate")
    flat_rebate_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Flat Rebate Option")
    business_development_fund_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Business Development Fund Left Option")
    business_development_fund = models.IntegerField(blank=True, null=True, verbose_name="Business Development Fund")
    business_development_fund_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Business Development Fund Option")
    payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Payment Terms Left Option")
    payment_terms = models.CharField(max_length=200, blank=True, null=True, verbose_name="Payment Terms")
    early_payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Early Payment Terms Left Option")
    early_payment_terms = models.CharField(max_length=200, blank=True, null=True, verbose_name="Early Payment Terms")
    early_payment_discount_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Early Payment Discount Left Option")
    early_payment_discount = models.IntegerField(blank=True, null=True, verbose_name="Early Payment Discount")
    early_payment_discount_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Early Payment Discount Option")
    cross_docking_allowance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cross Docking Allowance Left Option")
    cross_docking_allowance = models.IntegerField(blank=True, null=True, verbose_name="Cross Docking Allowance")
    cross_docking_allowance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cross Docking Allowance Option")
    east_malaysia_orders_allowance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="East Malaysia Orders Allowance Left Option")
    east_malaysia_orders_allowance = models.IntegerField(blank=True, null=True, verbose_name="East Malaysia Orders Allowance")
    east_malaysia_orders_allowance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="East Malaysia Orders Allowance Option")
    damage_good_allowance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Damage Good Allowance Left Option")
    damage_good_allowance = models.IntegerField(blank=True, null=True, verbose_name="Damage Good Allowance")
    damage_good_allowance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Damage Good Allowance Option")
    non_compliance_packaging_allowance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Non-compliance Packaging Allowance Left Option")
    non_compliance_packaging_allowance = models.IntegerField(blank=True, null=True, verbose_name="Non-compliance Packaging Allowance")
    non_compliance_packaging_allowance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Non-compliance Packaging Allowance Option")
    purchase_order_fulfillment_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Purchase Order Fulfillment Left Option")
    purchase_order_fulfillment = models.IntegerField(blank=True, null=True, verbose_name="Purchase Order Fulfillment")
    purchase_order_fulfillment_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Purchase Order Fulfillment Option")
    unfulfilled_penalty_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Unfulfilled Penalty Left Option")
    unfulfilled_penalty = models.IntegerField(blank=True, null=True, verbose_name="Unfulfilled Penalty")
    unfulfilled_penalty_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Unfulfilled Penalty Option")
    lost_of_profit_penalty_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lost of Profit Penalty Left Option")
    lost_of_profit_penalty = models.IntegerField(blank=True, null=True, verbose_name="Lost of Profit Penalty")
    lost_of_profit_penalty_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lost of Profit Penalty Option")
    purchase_order_lead_time_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Purchase Order Lead Time Left Option")
    purchase_order_lead_time = models.CharField(max_length=200, blank=True, null=True, verbose_name="Purchase Order Lead Time")
    purchase_order_lead_time_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Purchase Order Lead Time Option")
    lead_time_penalty_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lead Time Penalty Left Option")
    lead_time_penalty = models.IntegerField(blank=True, null=True, verbose_name="Lead Time Penalty")
    lead_time_penalty_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Lead Time Penalty Option")
    account_administration_fee_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Account Administration Fee Left Option")
    account_administration_fee = models.IntegerField(blank=True, null=True, verbose_name="Account Administration Fee")
    account_administration_fee_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Account Administration Fee Option")
    product_registration_fee_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Product Registration Fee Left Option")
    product_registration_fee = models.IntegerField(blank=True, null=True, verbose_name="Product Registration Fee")
    product_registration_fee_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="Product Registration Fee Option")
    sku_replacement_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="SKU Replacement Left Option")
    sku_replacement = models.IntegerField(blank=True, null=True, verbose_name="SKU Replacement")
    sku_replacement_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="SKU Replacement Option")
    new_item_listing_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="New Item Listing Left Option")
    new_item_listing = models.CharField(max_length=200, blank=True, null=True, verbose_name="New Item Listing")
    new_item_listing_option = models.CharField(max_length=200, blank=True, null=True, verbose_name="New Item Listing Option")
    new_item_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Left Option')
    new_item_first_order_discount = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount')
    new_item_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount 2 Left Option')
    new_item_first_order_discount_2 = models.IntegerField(blank=True, null=True, verbose_name='New Item First Order Discount 2')
    new_item_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Option')
    new_store_opening_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Left Option')
    new_store_opening = models.IntegerField(blank=True, null=True, verbose_name='New Store Opening')
    new_store_opening_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Option')
    refurbish_store_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Left Option')
    refurbish_store = models.IntegerField(blank=True, null=True, verbose_name='Refurbish Store')
    refurbish_store_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Option')
    anniversary_sales_allowance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Left Option')
    anniversary_sales_allowance = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Sales Allowance')
    anniversary_sales_allowance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Option')
    anniversary_orders_rebate_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Left Option')
    anniversary_orders_rebate = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Orders Rebate')
    anniversary_orders_rebate_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Option')
    new_store_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Left Option')
    new_store_first_order_discount = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount')
    new_store_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount 2 Left Option')
    new_store_first_order_discount_2 = models.IntegerField(blank=True, null=True, verbose_name='New Store First Order Discount 2')
    new_store_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Option')
    anniversary_sales_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Left Option')
    anniversary_sales = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Sales')
    anniversary_sales_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Option')
    chinese_new_year_sales_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Left Option')
    chinese_new_year_sales = models.IntegerField(blank=True, null=True, verbose_name='Chinese New Year Sales')
    chinese_new_year_sales_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Option')
    hari_raya_sales_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Left Option')
    hari_raya_sales = models.IntegerField(blank=True, null=True, verbose_name='Hari Raya Sales')
    hari_raya_sales_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Option')
    christmas_sales_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Left Option')
    christmas_sales = models.IntegerField(blank=True, null=True, verbose_name='Christmas Sales')
    christmas_sales_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Option')
    in_store_display_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='In-Store Display Left Option')
    in_store_display = models.IntegerField(blank=True, null=True, verbose_name='In-Store Display')
    in_store_display_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='In-Store Display Option')
    press_advertisement_n_mailer_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Press Advertisement and Mailer Left Option')
    press_advertisement_n_mailer = models.IntegerField(blank=True, null=True, verbose_name='Press Advertisement and Mailer')
    press_advertisement_n_mailer_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Press Advertisement and Mailer Option')
    adhoc_support_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Adhoc Support Left Option')
    adhoc_support = models.IntegerField(blank=True, null=True, verbose_name='Adhoc Support')
    adhoc_support_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Adhoc Support Option')
    crm_event_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Left Option')
    crm_event = models.IntegerField(blank=True, null=True, verbose_name='CRM Event')
    crm_event_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Option')
    marketing_event_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Left Option')
    marketing_event = models.IntegerField(blank=True, null=True, verbose_name='Marketing Event')
    marketing_event_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Option')
    concourse_event_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Left Option')
    concourse_event = models.IntegerField(blank=True, null=True, verbose_name='Concourse Event')
    concourse_event_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Option')
    system_setup_n_maintenance_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup and Maintenance Left Option')
    system_setup_n_maintenance = models.IntegerField(blank=True, null=True, verbose_name='System Setup and Maintenance')
    system_setup_n_maintenance_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup and Maintenance Option')
    digital_communication_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Left Option')
    digital_communication = models.IntegerField(blank=True, null=True, verbose_name='Digital Communication')
    digital_communication_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Option')
    social_media_post_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Left Option')
    social_media_post = models.IntegerField(blank=True, null=True, verbose_name='Social Media Post')
    social_media_post_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Option')
    market_place_event_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Left Option')
    market_place_event = models.IntegerField(blank=True, null=True, verbose_name='Market Place Event')
    market_place_event_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Market Place Event Option')
    normal_items_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Normal Items Left Option')
    normal_items = models.IntegerField(blank=True, null=True, verbose_name='Normal Items')
    normal_items_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Normal Items Option')
    best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Best Buy Items Left Option')
    best_buy_items = models.IntegerField(blank=True, null=True, verbose_name='Best Buy Items')
    best_buy_items_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Best Buy Items Option')
    super_best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Super Best Buy Items Left Option')
    super_best_buy_items = models.IntegerField(blank=True, null=True, verbose_name='Super Best Buy Items')
    super_best_buy_items_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Super Best Buy Items Option')
    mark_down_items_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mark Down Items Left Option')
    mark_down_items = models.IntegerField(blank=True, null=True, verbose_name='Mark Down Items')
    mark_down_items_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mark Down Items Option')
    number_50_percent_discount_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='50% Discount Left Option')
    number_50_percent_discount = models.IntegerField(blank=True, null=True, verbose_name='50% Discount')
    number_50_percent_discount_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='50% Discount Option')
    data_sharing_subscription_left_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Subscription Left Option')
    data_sharing_subscription = models.IntegerField(blank=True, null=True, verbose_name='Data Sharing Subscription')
    data_sharing_subscription_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Subscription Option')
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Sales and Quantity Performance by Store vs Last Year Performance')
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Sales and Quantity Performance by Store vs Last Year Performance Option')
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Sales and Quantity Performance by Store vs Last Year Performance')
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Sales and Quantity Performance by Store vs Last Year Performance Option')
    weekly_stock_listing_by_sku = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Stock Listing by SKU')
    weekly_stock_listing_by_sku_option = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Stock Listing by SKU Option')
    general_complicance = models.CharField(max_length=200, blank=True, null=True, verbose_name='General Complicance')
    return_condition = models.CharField(max_length=200, blank=True, null=True, verbose_name='Returning Condition')
    price_n_billing = models.CharField(max_length=200, blank=True, null=True, verbose_name='Price and Billing')
    effective_date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Effective Date')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Created at")
    created_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Created by")
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name="Updated at")
    updated_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Updated by")
    submit_date = models.DateTimeField(blank=True, null=True, verbose_name="Submit Date")
    submit_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Submit by")
    approve_date = models.DateTimeField(blank=True, null=True, verbose_name="Approve Date")
    approve_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Approve by")
    reject_at = models.DateTimeField(blank=True, null=True, verbose_name="Reject at")
    reject_by = models.CharField(max_length=20, blank=True, null=True, verbose_name="Reject by")
    list_status = models.CharField(max_length=20, blank=True, null=True, verbose_name="List Status")

    class Meta:
        managed = False
        db_table = 'tta_list'
        ordering = ('updated_at','refno')

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  