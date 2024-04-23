from django.db import models

# Create your models here.
class RimsBanner(models.Model):
    banner_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    concept_guid = models.CharField(max_length=32, blank=True, null=True)
    concept = models.CharField(max_length=100, blank=True, null=True)
    concept_inactive = models.SmallIntegerField(blank=True, null=True)
    branch_guid = models.CharField(max_length=32, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    branch_inactive = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rims_banner'
        unique_together = (('banner_guid', 'customer_guid'),)
        #ordering = ('concept')

    def __str__(self):
        return self.banner_guid

    def get_absolute_url(self):
        return f'/{self.banner_guid}/' 

