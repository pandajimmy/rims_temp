from django.db import models

class FormOption(models.Model):
    option_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Option guid')
    option_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Option Type')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'form_option'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'  