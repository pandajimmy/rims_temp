from django.db import models

class SetUser(models.Model):
    customer_guid = models.CharField(max_length=32)
    loc_count = models.SmallIntegerField(blank=True, null=True)
    loc_group = models.CharField(max_length=32, blank=True, null=True)
    user_group_guid = models.CharField(max_length=32, blank=True, null=True)
    user_group_name = models.CharField(max_length=120, blank=True, null=True)
    user_guid = models.CharField(primary_key=True, max_length=32)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=15, blank=True, null=True)
    user_name = models.CharField(max_length=60, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_instance = models.CharField(max_length=120, blank=True, null=True)
    user_instance_variable = models.CharField(max_length=120, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    mobile_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_user'
        unique_together = (('user_guid', 'customer_guid'),)
        ordering = ('user_id',)

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return f'/{self.user_id}/'  