# Generated by Django 5.0.6 on 2024-05-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TtaListDisplayIncentiveTable',
            fields=[
                ('tta_display_incentive_table_guid', models.CharField(blank=True, editable=False, max_length=36, primary_key=True, serialize=False, verbose_name='TTA List Display Incentive Table guid')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('outlet', models.CharField(blank=True, max_length=200, null=True, verbose_name='Outlet')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='Percent')),
            ],
            options={
                'verbose_name': 'TTA List Display Incentive Table Detail',
                'verbose_name_plural': 'TTA List Display Incentive Table Details',
                'db_table': 'tta_displayincentive',
                'ordering': ('list_guid',),
                'managed': False,
            },
        ),
    ]
