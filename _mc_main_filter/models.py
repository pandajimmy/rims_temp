from django.db import models

class MainFilter(models.Model):
    main_filter_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Main Filter Globally Unique Identifier')
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name='Code')
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=200, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=200, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'main_filter'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'  