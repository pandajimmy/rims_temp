from django.db import models

class DesignMainTemplate(models.Model):
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    main_guid = models.CharField(primary_key=True, max_length=32)
    main_name = models.CharField(max_length=100, blank=True, null=True)
    main_description = models.CharField(max_length=250, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_main_template'
        ordering = ('main_name',)

    def __str__(self):
        return self.main_name

    def get_absolute_url(self):
        return f'/{self.main_name}/'  