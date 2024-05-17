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
            name='TtaListPaymentNDiscount',
            fields=[
                ('list_guid', models.OneToOneField(db_column='list_guid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='_mc_tta_list.ttalist', verbose_name='List guid')),
                ('list_link_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='List Link guid')),
                ('discount_guid', models.CharField(blank=True, editable=False, max_length=36, verbose_name='Discount guid')),
                ('revision', models.CharField(blank=True, max_length=100, null=True, verbose_name='Revision')),
                ('customer_guid', models.CharField(max_length=32, verbose_name='Customer guid')),
                ('refno', models.CharField(editable=False, max_length=20, verbose_name='Reference No.')),
                ('payment_terms_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Payment Terms Type')),
                ('early_payment_terms_value', models.FloatField(blank=True, null=True, verbose_name='Early Payment Terms Value')),
                ('early_payment_terms_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Early Payment Terms Type')),
                ('early_payment_discount_value', models.FloatField(blank=True, null=True, verbose_name='Early Payment Discount Value')),
                ('early_payment_discount_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Early Payment Discount Type')),
                ('early_payment_discount_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Early Payment Discount Value Type')),
                ('prompt_payment_discount_value', models.FloatField(blank=True, null=True, verbose_name='Prompt Payment Discount Value')),
                ('prompt_payment_discount_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prompt Payment Discount Type')),
                ('prompt_payment_discount_value_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prompt Payment Discount Value Type')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Created by')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'TTA List Payment and Discount Detail',
                'verbose_name_plural': 'TTA List Payment and Discount Details',
                'db_table': 'tta_list_paymentndiscount',
                'ordering': ('refno',),
                'managed': False,
            },
        ),
    ]