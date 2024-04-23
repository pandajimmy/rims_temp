from django.db import models

class TtaListStatus(models.Model):
    status_key = models.CharField(primary_key=True, max_length=30)
    status_description = models.CharField(max_length=32, blank=True, null=True)
    status_process = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tta_list_status'
        ordering = ('status_description',)

    def __str__(self):
        return self.status_description

    def get_absolute_url(self):
        return f'/{self.status_description}/'  