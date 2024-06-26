# Generated by Django 3.2.7 on 2021-10-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignComponent',
            fields=[
                ('component_guid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('seq', models.IntegerField(blank=True, null=True)),
                ('cols_size', models.IntegerField(blank=True, null=True)),
                ('sm_size', models.IntegerField(blank=True, null=True)),
                ('md_size', models.IntegerField(blank=True, null=True)),
                ('lg_size', models.IntegerField(blank=True, null=True)),
                ('xl_size', models.IntegerField(blank=True, null=True)),
                ('group', models.CharField(blank=True, max_length=100, null=True)),
                ('input_type', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('option_url', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'design_component',
                'ordering': ('seq',),
                'managed': False,
            },
        ),
    ]
