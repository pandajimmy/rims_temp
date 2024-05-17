# Generated by Django 5.0.6 on 2024-05-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfileTable',
            fields=[
                ('customer_guid', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Customer guid')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer Name')),
                ('customer_regno', models.CharField(blank=True, max_length=30, null=True, verbose_name='Customer Registration No.')),
                ('customer_gstno', models.CharField(blank=True, max_length=30, null=True, verbose_name='Customer GST No.')),
                ('customer_taxcode', models.CharField(blank=True, max_length=30, null=True, verbose_name='Customer Tax Code')),
                ('customer_add1', models.CharField(blank=True, max_length=60, null=True, verbose_name='Customer Address 1')),
                ('customer_add2', models.CharField(blank=True, max_length=60, null=True, verbose_name='Customer Address 2')),
                ('customer_add3', models.CharField(blank=True, max_length=60, null=True, verbose_name='Customer Address 3')),
                ('customer_add4', models.CharField(blank=True, max_length=60, null=True, verbose_name='Customer Address 4')),
                ('customer_postcode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Customer Postcode')),
                ('customer_state', models.CharField(blank=True, max_length=20, null=True, verbose_name='Customer State')),
                ('customer_country', models.CharField(blank=True, max_length=25, null=True, verbose_name='Customer Country')),
                ('customer_tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='Customer Tel No.')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Created by')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Updated by')),
            ],
            options={
                'db_table': 'customer_profile',
                'ordering': ('customer_name',),
                'managed': False,
            },
        ),
    ]
