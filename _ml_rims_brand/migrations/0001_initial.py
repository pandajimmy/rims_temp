# Generated by Django 5.0.6 on 2024-05-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RimsBrand',
            fields=[
                ('brand_guid', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Branch guid')),
                ('customer_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='Customer guid')),
                ('mcode', models.CharField(blank=True, db_column='MCode', max_length=10, null=True, verbose_name='M Code')),
                ('code', models.CharField(blank=True, db_column='Code', max_length=10, null=True, verbose_name='Code')),
                ('description', models.CharField(blank=True, db_column='Description', max_length=40, null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'rims_brand',
                'managed': False,
            },
        ),
    ]