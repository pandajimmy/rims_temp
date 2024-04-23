from django.db import models

class AccUser(models.Model):
    acc_user_guid = models.CharField(primary_key=True, max_length=32)
    acc_user_id = models.CharField(max_length=255, blank=True, null=True)
    acc_user_password = models.CharField(max_length=15, blank=True, null=True)
    acc_user_name = models.CharField(max_length=60, blank=True, null=True)
    acc_user_instance = models.CharField(max_length=120, blank=True, null=True)
    acc_user_instance_variable = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    acc_guid = models.CharField(max_length=32)
    acc_name = models.CharField(max_length=120, blank=True, null=True)
    user_count = models.CharField(max_length=120, blank=True, null=True)
    driver_count = models.CharField(max_length=120, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    acc_user_location = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_user'

    def __str__(self):
        return self.acc_user_id

    def get_absolute_url(self):
        return f'/{self.acc_user_id}/'  