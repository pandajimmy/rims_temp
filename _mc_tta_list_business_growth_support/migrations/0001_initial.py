# Generated by Django 5.0.6 on 2024-05-16 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('_mc_tta_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TtaListBusinessGrowthSupport',
            fields=[
                ('list_guid', models.OneToOneField(db_column='list_guid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='_mc_tta_list.ttalist', verbose_name='List guid')),
                ('list_link_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='List Link guid')),
                ('bgs_guid', models.CharField(blank=True, editable=False, max_length=36, verbose_name='Business Growth Support guid')),
                ('revision', models.CharField(blank=True, max_length=100, null=True, verbose_name='Revision')),
                ('customer_guid', models.CharField(max_length=32, verbose_name='Customer guid')),
                ('refno', models.CharField(editable=False, max_length=20, verbose_name='Reference No.')),
                ('category_development_fund_value', models.FloatField(blank=True, null=True, verbose_name='Category Development Fund Value')),
                ('category_development_fund_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Category Development Fund Type')),
                ('category_development_fund_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Category Development Fund Value Type')),
                ('business_development_fund_value', models.FloatField(blank=True, null=True, verbose_name='Business Development Fund Value')),
                ('business_development_fund_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Business Development Fund Type')),
                ('business_development_fund_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Business Development Fund Value Type')),
                ('data_sharing_fee_value', models.FloatField(blank=True, null=True, verbose_name='Data Sharing Fee Value')),
                ('data_sharing_fee_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Data Sharing Fee Type')),
                ('data_sharing_fee_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Data Sharing Fee Value Type')),
                ('new_store_opening_value', models.FloatField(blank=True, null=True, verbose_name='New Store Opening Value')),
                ('new_store_opening_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store Opening Type')),
                ('new_store_opening_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store Opening Value Type')),
                ('new_store_opening_date_to', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store Opening Date To')),
                ('new_store_opening_date_from', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store Opening Date From')),
                ('new_store_first_order_discount_value1', models.FloatField(blank=True, null=True, verbose_name='New Store First Order Discount Value 1')),
                ('new_store_first_order_discount_value2', models.FloatField(blank=True, null=True, verbose_name='New Store First Order Discount Value 2')),
                ('new_store_first_order_discount_type1', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store First Order Discount Type 1')),
                ('new_store_first_order_discount_type2', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store First Order Discount Type 2')),
                ('new_store_first_order_discount_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='New Store First Order Discount Value Type')),
                ('refurbish_store_value', models.FloatField(blank=True, null=True, verbose_name='Refurbish Store Value')),
                ('refurbish_store_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Refurbish Store Type')),
                ('refurbish_store_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Refurbish Store Value Type')),
                ('refurbish_store_date_to', models.CharField(blank=True, max_length=200, null=True, verbose_name='Refurbish Store Date To')),
                ('refurbish_store_date_from', models.CharField(blank=True, max_length=200, null=True, verbose_name='Refurbish Store Date From')),
                ('anniversary_sales_allowance_value', models.FloatField(blank=True, null=True, verbose_name='Anniversary Sales Allowance Value')),
                ('anniversary_sales_allowance_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Sales Allowance Type')),
                ('anniversary_sales_allowance_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Sales Allowance Value Type')),
                ('anniversary_sales_allowance_date_to', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Sales Allowance Date To')),
                ('anniversary_sales_allowance_date_from', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Sales Allowance Date From')),
                ('anniversary_orders_rebate_value', models.FloatField(blank=True, null=True, verbose_name='Anniversary Orders Rebate Value')),
                ('anniversary_orders_rebate_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Orders Rebate Type')),
                ('anniversary_orders_rebate_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Orders Rebate Value Type')),
                ('anniversary_orders_rebate_date_to', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Orders Rebate Date To')),
                ('anniversary_orders_rebate_date_from', models.CharField(blank=True, max_length=200, null=True, verbose_name='Anniversary Orders Rebate Date From')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Created by')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'TTA List Business Growth Support Detail',
                'verbose_name_plural': 'TTA List Business Growth Support Details',
                'db_table': 'tta_list_businessgrowthsupport',
                'ordering': ('refno',),
                'managed': False,
            },
        ),
    ]
