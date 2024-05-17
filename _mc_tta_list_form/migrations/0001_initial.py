# Generated by Django 5.0.6 on 2024-05-16 10:46

import _mc_tta_list_form.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TtaListForm',
            fields=[
                ('list_guid_c', models.CharField(default=_mc_tta_list_form.models.generate_uuid, max_length=32, primary_key=True, serialize=False, verbose_name='List guid C')),
                ('tab_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='Tab guid')),
                ('group', models.CharField(blank=True, max_length=200, null=True, verbose_name='Group')),
                ('seq', models.IntegerField(blank=True, null=True, verbose_name='Sequence')),
                ('key_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Key Description')),
                ('left_option', models.CharField(blank=True, max_length=100, null=True, verbose_name='Left Option')),
                ('varchar_1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Var Char 1')),
                ('type_1', models.CharField(blank=True, max_length=32, null=True, verbose_name='Type 1')),
                ('val_1', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Value 1')),
                ('text_1', models.TextField(blank=True, null=True, verbose_name='Text 1')),
                ('type_2', models.CharField(blank=True, max_length=32, null=True, verbose_name='Type 2')),
                ('val_2', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Value 2')),
                ('type_3', models.CharField(blank=True, max_length=32, null=True, verbose_name='Type 3')),
                ('val_3', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Value 3')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('created_by', models.CharField(blank=True, max_length=20, null=True, verbose_name='Created by')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated at')),
                ('updated_by', models.CharField(blank=True, max_length=20, null=True, verbose_name='Updated by')),
            ],
            options={
                'db_table': 'tta_list_form',
                'ordering': ('group',),
                'managed': False,
            },
        ),
    ]