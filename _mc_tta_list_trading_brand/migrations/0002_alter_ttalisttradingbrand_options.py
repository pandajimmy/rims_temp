# Generated by Django 5.0.6 on 2024-05-27 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_mc_tta_list_trading_brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ttalisttradingbrand',
            options={'managed': False, 'ordering': ('list_guid',), 'verbose_name': 'TTA List Trading Brand Detail', 'verbose_name_plural': 'TTA List Trading Brands Details'},
        ),
    ]
