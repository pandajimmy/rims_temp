# Generated by Django 3.2.7 on 2021-10-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignTab',
            fields=[
                ('tab_guid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('sequence', models.SmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'design_tab',
                'ordering': ('sequence',),
                'managed': False,
            },
        ),
    ]
