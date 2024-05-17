# Generated by Django 5.0.6 on 2024-05-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RimsPayTerm',
            fields=[
                ('customer_guid', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Customer guid')),
                ('code', models.CharField(db_column='Code', max_length=15, verbose_name='Code')),
                ('description', models.CharField(blank=True, db_column='Description', max_length=60, null=True, verbose_name='Description')),
                ('setactive', models.SmallIntegerField(blank=True, db_column='SetActive', null=True, verbose_name='Set Active')),
                ('imported_at', models.DateTimeField(blank=True, null=True, verbose_name='Imported at')),
                ('sync_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='Sync guid')),
            ],
            options={
                'db_table': 'rims_pay_term',
                'ordering': ('customer_guid', 'description'),
                'managed': False,
            },
        ),
    ]
