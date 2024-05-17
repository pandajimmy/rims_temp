from django.db import models

class DesignMainTemplate(models.Model):
    customer_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='Customer guid')
    main_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Main guid')
    main_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Main Name')
    main_description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Main Description')
    isactive = models.IntegerField(blank=True, null=True, verbose_name='Is Active')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Updated by')

    class Meta:
        managed = False
        db_table = 'design_main_template'
        ordering = ('main_name',)

    def __str__(self):
        return self.main_name

    def get_absolute_url(self):
        return f'/{self.main_name}/'  