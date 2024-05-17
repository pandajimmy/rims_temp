# Generated by Django 5.0.6 on 2024-05-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUrl',
            fields=[
                ('url_guid', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='URL guid')),
                ('customer_guid', models.CharField(blank=True, max_length=32, null=True, verbose_name='Customer guid')),
                ('customer_url', models.CharField(blank=True, max_length=120, null=True, verbose_name='Customer URL')),
                ('key', models.CharField(blank=True, max_length=60, null=True, verbose_name='Key')),
                ('userid', models.CharField(blank=True, max_length=32, null=True, verbose_name='User ID')),
                ('userpass', models.CharField(blank=True, max_length=32, null=True, verbose_name='User Password')),
                ('isactive', models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Created at')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
            ],
            options={
                'db_table': 'customer_url',
                'managed': False,
            },
        ),
    ]