from django.db import models

class TtaListDetails(models.Model):
    # Main Details
    list_guid = models.CharField(primary_key=True, max_length=32, verbose_name='List Globally Unique Identifier')
    customer_guid = models.CharField(max_length=32, verbose_name='Customer Globally Unique Identifier')
    refno = models.CharField(max_length=20, verbose_name='Reference Number')

    # Supplier ID and Name
    supplier_guid = models.CharField(max_length=32, verbose_name='Supplier Globally Unique Identifier')
    supplier_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Supplier Name')
    
    # Bill of Supplier
    bill_supp_guid = models.CharField(max_length=32, verbose_name='Bill Supplier Globally Unique Identifier')
    bill_supp_code = models.CharField(max_length=32, verbose_name='Bill Supplier Code')
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Bill Supplier Name')

    # Other Details
    negotiation_year = models.TextField(blank=True, null=True, verbose_name='Negotiation Year')
    co_reg_no = models.CharField(max_length=32, blank=True, null=True, verbose_name='Company Registration Number')
    tta_period_from = models.CharField(max_length=200, blank=True, null=True, verbose_name='TTA Period From')
    tta_period_to = models.CharField(max_length=200, blank=True, null=True, verbose_name='TTA Period To')
    internal_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name='Internal PIC')
    
    # Trading Information
    trading_group = models.CharField(max_length=200, blank=True, null=True, verbose_name='Trading Group')
    trading_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Trading Type')
    delivery_mode = models.CharField(max_length=200, blank=True, null=True, verbose_name='Delivery Mode')
    returnable = models.CharField(max_length=200, blank=True, null=True, verbose_name='Returnable')
    
    # Supplier Person In Charge Information
    supplier_pic = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge')
    supplier_pic_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Name')
    supplier_pic_position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Position')
    supplier_pic_contact = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Contact')
    supplier_pic_email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Supplier Person In Charge Email')
    
    #Banner
    banner = models.CharField(max_length=200, blank=True, null=True, verbose_name='Banner')

    #Outlet
    outlet = models.CharField(max_length=200, blank=True, null=True, verbose_name='Outlet')
    
    # Target Purchase Per Year
    target_purchase_per_year_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Per Year Value Type')
    target_purchase_per_year = models.IntegerField(blank=True, null=True, verbose_name='Target Purchase Per Year')
    target_purchase_per_year_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Target Purchase Per Year Type')

    # Flat Rebate
    flat_rebate_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Flat Rebate Value Type')
    flat_rebate = models.IntegerField(blank=True, null=True, verbose_name='Flat Rebate')
    flat_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Flat Rebate Type')

    # Business Development Fund
    business_development_fund_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Business Development Fund Value Type')
    business_development_fund = models.IntegerField(blank=True, null=True, verbose_name='Business Development Fund')
    business_development_fund_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Business Development Fund Type')

    # Payment Terms
    payment_terms_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Payment Terms Value Type')
    payment_terms = models.CharField(max_length=200, blank=True, null=True, verbose_name='Payment Terms')

    # Early Payment Terms
    early_payment_terms_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Terms Value Type')
    early_payment_terms = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Terms')

    # Early Payment Discount
    early_payment_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Value Type')
    early_payment_discount = models.IntegerField(blank=True, null=True, verbose_name='Early Payment Discount')
    early_payment_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Early Payment Discount Type')

    # Cross Docking Allowance
    cross_docking_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cross Docking Allowance Value Type')
    cross_docking_allowance = models.IntegerField(blank=True, null=True, verbose_name='Cross Docking Allowance')
    cross_docking_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cross Docking Allowance Type')

    # East Malaysia Orders Allowance
    east_malaysia_orders_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='East Malaysia Orders Allowance Value Type')
    east_malaysia_orders_allowance = models.IntegerField(blank=True, null=True, verbose_name='East Malaysia Orders Allowance')
    east_malaysia_orders_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='East Malaysia Orders Allowance Type')

    # Damage Good Allowance
    damage_good_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Damage Good Allowance Value Type')
    damage_good_allowance = models.IntegerField(blank=True, null=True, verbose_name='Damage Good Allowance')
    damage_good_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Damage Good Allowance Type')

    # Non-compliance Packaging Allowance
    non_compliance_packaging_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non-compliance Packaging Allowance Value Type')
    non_compliance_packaging_allowance = models.IntegerField(blank=True, null=True, verbose_name='Non-compliance Packaging Allowance')
    non_compliance_packaging_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Non-compliance Packaging Allowance Type')

    # Purchase Order Fulfillment
    purchase_order_fulfillment_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Fulfillment Value Type')
    purchase_order_fulfillment = models.IntegerField(blank=True, null=True, verbose_name='Purchase Order Fulfillment')
    purchase_order_fulfillment_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Fulfillment Type')

    # Unfulfilled Penalty
    unfulfilled_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unfulfilled Penalty Value Type')
    unfulfilled_penalty = models.IntegerField(blank=True, null=True, verbose_name='Unfulfilled Penalty')
    unfulfilled_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Unfulfilled Penalty Type')

    # Lost of Profit Penalty
    lost_of_profit_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lost of Profit Penalty Value Type')
    lost_of_profit_penalty = models.IntegerField(blank=True, null=True, verbose_name='Lost of Profit Penalty')
    lost_of_profit_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lost of Profit Penalty Type')

    # Purchase Order Lead Time
    purchase_order_lead_time_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Lead Time Value Type')
    purchase_order_lead_time = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Lead Time')
    purchase_order_lead_time_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Purchase Order Lead Time Type')

    # Lead Time Penalty
    lead_time_penalty_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lead Time Penalty Value Type')
    lead_time_penalty = models.IntegerField(blank=True, null=True, verbose_name='Lead Time Penalty')
    lead_time_penalty_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Lead Time Penalty Type')

    # Account Administration Fee
    account_administration_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Account Administration Fee Value Type')
    account_administration_fee = models.IntegerField(blank=True, null=True, verbose_name='Account Administration Fee')
    account_administration_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Account Administration Fee Type')

    # Product Registration Fee
    product_registration_fee_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Product Registration Fee Value Type')
    product_registration_fee = models.IntegerField(blank=True, null=True, verbose_name='Product Registration Fee')
    product_registration_fee_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Product Registration Fee Type')

    # SKU Replacement
    sku_replacement_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='SKU Replacement Value Type')
    sku_replacement = models.IntegerField(blank=True, null=True, verbose_name='SKU Replacement')
    sku_replacement_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='SKU Replacement Type')

    # New Item Listing
    new_item_listing_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item Listing Value Type')
    new_item_listing = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item Listing')
    new_item_listing_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item Listing Type')

    # New Item First Order Discount
    new_item_first_order_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Value Type')
    new_item_first_order_discount_value = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Value')
    new_item_first_order_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Item First Order Discount Type')

    # New Store Opening
    new_store_opening_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Value Type')
    new_store_opening_value = models.IntegerField(blank=True, null=True, verbose_name='New Store Opening Value')
    new_store_opening_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store Opening Type')

    # Refurbish Store
    refurbish_store_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Value Type')
    refurbish_store_value = models.IntegerField(blank=True, null=True, verbose_name='Refurbish Store Value')
    refurbish_store_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Refurbish Store Type')

    # Anniversary Sales Allowance
    anniversary_sales_allowance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Value Type')
    anniversary_sales_allowance_value = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Sales Allowance Value')
    anniversary_sales_allowance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Allowance Type')

    # Anniversary Orders Rebate
    anniversary_orders_rebate_value_type = models.CharField(max_length=200, blank=True, null=True,  verbose_name='Anniversary Orders Rebate Value Type')
    anniversary_orders_rebate_value = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Orders Rebate Value')
    anniversary_orders_rebate_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Orders Rebate Type')

    # New Store First Order Discount
    new_store_first_order_discount_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Value Type')
    new_store_first_order_discount_value = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Value')
    new_store_first_order_discount_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='New Store First Order Discount Type')

    # Anniversary Sales
    anniversary_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Value Type')
    anniversary_sales_value = models.IntegerField(blank=True, null=True, verbose_name='Anniversary Sales Value')
    anniversary_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Anniversary Sales Type')

    # Seasonal Sales
    chinese_new_year_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Value Type')
    chinese_new_year_sales_value = models.IntegerField(blank=True, null=True, verbose_name='Chinese New Year Sales Value')
    chinese_new_year_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Chinese New Year Sales Type')

    hari_raya_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Value Type')
    hari_raya_sales_value = models.IntegerField(blank=True, null=True, verbose_name='Hari Raya Sales Value')
    hari_raya_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Hari Raya Sales Type')

    christmas_sales_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Value Type')
    christmas_sales_value = models.IntegerField(blank=True, null=True, verbose_name='Christmas Sales Value')
    christmas_sales_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Christmas Sales Type')

    # Marketing and Promotion
    in_store_display_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='In-store Display Value Type')
    in_store_display_value = models.IntegerField(blank=True, null=True, verbose_name='In-store Display Value')
    in_store_display_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='In-store Display Type')

    press_advertisement_n_mailer_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Press Advertisement and Mailer Value Type')
    press_advertisement_n_mailer_value = models.IntegerField(blank=True, null=True, verbose_name='Press Advertisement and Mailer Value')
    press_advertisement_n_mailer_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Press Advertisement and Mailer Type')

    adhoc_support_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Adhoc Support Value Type')
    adhoc_support_value = models.IntegerField(blank=True, null=True, verbose_name='Adhoc Support Value')
    adhoc_support_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Adhoc Support Type')

    crm_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Value Type')
    crm_event_value = models.IntegerField(blank=True, null=True, verbose_name='CRM Event Value')
    crm_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='CRM Event Type')

    marketing_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketing Event Value Type')
    marketing_event_value = models.IntegerField(blank=True, null=True, verbose_name='Marketing Event Value')
    marketing_event_type = models.CharField(max_length=200, blank=True, null=True,  verbose_name='Marketing Event Type')

    concourse_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Concourse Event Value Type')
    concourse_event_value = models.IntegerField(blank=True, null=True, verbose_name='Concourse Event Value')
    concourse_event_type = models.CharField(max_length=200, blank=True, null=True,  verbose_name='Concourse Event Type')

    system_setup_n_maintenance_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup and Maintenance Value Type')
    system_setup_n_maintenance_value = models.IntegerField(blank=True, null=True, verbose_name='System Setup and Maintenance Value')
    system_setup_n_maintenance_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='System Setup and Maintenance Type')

    digital_communication_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Value Type')
    digital_communication_value = models.IntegerField(blank=True, null=True, verbose_name='Digital Communication Value')
    digital_communication_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Digital Communication Type')

    social_media_post_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Value Type')
    social_media_post_value = models.IntegerField(blank=True, null=True, verbose_name='Social Media Post Value')
    social_media_post_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Social Media Post Type')

    market_place_event_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketplace Event Value Type')
    market_place_event_value = models.IntegerField(blank=True, null=True, verbose_name='Marketplace Event Value')
    market_place_event_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Marketplace Event Type')

    # Inventory Management
    normal_items_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Normal Items Value Type')
    normal_items_value = models.IntegerField(blank=True, null=True, verbose_name='Normal Items Value')
    normal_items_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Normal Items Type')

    best_buy_items_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Best Buy Items Value Type')
    best_buy_items_value = models.IntegerField(blank=True, null=True, verbose_name='Best Buy Items Value')
    best_buy_items_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Best Buy Items Type')

    super_best_buy_items_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Super Best Buy Items Value Type')
    super_best_buy_items_value = models.IntegerField(blank=True, null=True, verbose_name='Super Best Buy Items Value')
    super_best_buy_items_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Super Best Buy Items Type')

    mark_down_items_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mark Down Items Value Type')
    mark_down_items_value = models.IntegerField(blank=True, null=True, verbose_name='Mark Down Items Value')
    mark_down_items_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mark Down Items Type')

    number_50_percent_discount_value_type = models.CharField(db_column='50_percent_discount_value_type', max_length=200, blank=True, null=True, verbose_name='50% Discount Value Type')
    number_50_percent_discount_value = models.IntegerField(db_column='50_percent_discount', blank=True, null=True, verbose_name='50% Discount Value')
    number_50_percent_discount_type = models.CharField(db_column='50_percent_discount_type', max_length=200, blank=True, null=True, verbose_name='50% Discount Type')

    # Data Management
    data_sharing_subscription_value_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Subscription Value Type')
    data_sharing_subscription_value = models.IntegerField(blank=True, null=True, verbose_name='Data Sharing Subscription Value')
    data_sharing_subscription_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Data Sharing Subscription Type')

    # Sales Performance Analysis
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Sales & Quantity Performance vs Last Year Performance')
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Sales & Quantity Performance vs Last Year Performance Type')

    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Sales & Quantity Performance vs Last Year Performance')
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Monthly Sales & Quantity Performance vs Last Year Performance Type')

    weekly_stock_listing_by_sku = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Stock Listing by SKU')
    weekly_stock_listing_by_sku_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Weekly Stock Listing by SKU Type')

    # General Compliance
    general_compliance = models.CharField(max_length=200, blank=True, null=True, verbose_name='General Compliance')

    # Returning Condition
    return_condition = models.CharField(max_length=200, blank=True, null=True, verbose_name="Returning Condition")

    # Price and Billing
    price_n_billing = models.CharField(max_length=200, blank=True, null=True, verbose_name='Price and Billing')

    #Status of the Tta List Details
    effective_date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Effective Date')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')
    created_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Created By')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated At')
    updated_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Updated By')
    submit_date = models.DateTimeField(blank=True, null=True, verbose_name='Submit Date')
    submit_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Submit By')
    approve_date = models.DateTimeField(blank=True, null=True, verbose_name='Approve Date')
    approve_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Approve By')
    reject_at = models.DateTimeField(blank=True, null=True, verbose_name='Reject Date')
    reject_by = models.CharField(max_length=32, blank=True, null=True, verbose_name='Reject By')
    list_status = models.CharField(max_length=20, blank=True, null=True, verbose_name='List Status')

    class Meta:
        managed = False
        db_table = 'tta_list'
        verbose_name = 'TTA List Detail'
        verbose_name_plural = 'TTA List Details'
        ordering = ('refno',)

    def __str__(self):
        return self.refno

    def get_absolute_url(self):
        return f'/{self.refno}/'  