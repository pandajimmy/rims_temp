# Generated by Django 5.0.6 on 2024-05-17 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_mc_tta_list_purchase_n_rebates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ttalistpurchasenrebates',
            options={'managed': False, 'ordering': ['list_guid__refno'], 'verbose_name': 'TTA List Purchase and Rebates Detail', 'verbose_name_plural': 'TTA List Purchase and Rebates Details'},
        ),
    ]