from django.db import models

class MainFilter(models.Model):
    main_filter_guid = models.CharField(primary_key=True, max_length=32)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_filter'
        ordering = ('description',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/{self.description}/'  