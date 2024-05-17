# Generated by Django 5.0.6 on 2024-05-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TtaListDetails',
            fields=[
                ('list_guid', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='List Globally Unique Identifier')),
                ('customer_guid', models.CharField(max_length=32, verbose_name='Customer Globally Unique Identifier')),
                ('refno', models.CharField(max_length=20, verbose_name='Reference Number')),
                ('supplier_guid', models.CharField(max_length=32, verbose_name='Supplier Globally Unique Identifier')),
                ('supplier_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Supplier Name')),
                ('bill_supp_guid', models.CharField(max_length=32, verbose_name='Bill Supplier Globally Unique Identifier')),
                ('bill_supp_code', models.CharField(max_length=32, verbose_name='Bill Supplier Code')),
                ('bill_supp_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Bill Supplier Name')),
                ('negotiation_year', models.TextField(blank=True, null=True, verbose_name='Negotiation Year')),
                ('co_reg_no', models.CharField(blank=True, max_length=32, null=True, verbose_name='Company Registration Number')),
                ('tta_period_from', models.CharField(blank=True, max_length=200, null=True, verbose_name='TTA Period From')),
                ('tta_period_to', models.CharField(blank=True, max_length=200, null=True, verbose_name='TTA Period To')),
                ('internal_pic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Internal PIC')),
                ('trading_group1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trading Group 1')),
                ('trading_group2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trading Group 2')),
                ('trading_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trading Type')),
                ('delivery_mode', models.CharField(blank=True, max_length=200, null=True, verbose_name='Delivery Mode')),
                ('returnable', models.CharField(blank=True, max_length=200, null=True, verbose_name='Returnable')),
                ('supplier_pic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Person In Charge')),
                ('supplier_pic_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Person In Charge Name')),
                ('supplier_pic_position', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Person In Charge Position')),
                ('supplier_pic_contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Person In Charge Contact')),
                ('supplier_pic_email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Supplier Person In Charge Email')),
                ('banner', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner')),
                ('outlet1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outlet 1')),
                ('outlet2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outlet 2')),
                ('effective_date', models.CharField(blank=True, max_length=200, null=True, verbose_name='Effective Date')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created At')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created By')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated At')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated By')),
                ('submit_date', models.DateTimeField(blank=True, null=True, verbose_name='Submit Date')),
                ('submit_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Submit By')),
                ('approve_date', models.DateTimeField(blank=True, null=True, verbose_name='Approve Date')),
                ('approve_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Approve By')),
                ('reject_at', models.DateTimeField(blank=True, null=True, verbose_name='Reject Date')),
                ('reject_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Reject By')),
                ('list_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='List Status')),
            ],
            options={
                'verbose_name': 'TTA List Detail',
                'verbose_name_plural': 'TTA List Details',
                'db_table': 'tta_list',
                'ordering': ('refno',),
                'managed': False,
            },
        ),
    ]
