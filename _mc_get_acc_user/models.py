from django.db import models

class AccUser(models.Model):
    acc_user_guid = models.CharField(primary_key=True, max_length=32, verbose_name='Account User Globally Unique Identifier')
    acc_user_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='Account User Identifier')
    acc_user_password = models.CharField(max_length=15, blank=True, null=True, verbose_name='Account User Password')
    acc_user_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='Account User Name')
    acc_user_instance = models.CharField(max_length=120, blank=True, null=True, verbose_name='Account User Instance')
    acc_user_instance_variable = models.CharField(max_length=120, blank=True, null=True, verbose_name='Account User Instance Variable')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='Updated by')
    acc_guid = models.CharField(max_length=32, verbose_name='Account Globally Unique Identifier')
    acc_name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Account Name')
    user_count = models.CharField(max_length=120, blank=True, null=True, verbose_name='Number of User')
    driver_count = models.CharField(max_length=120, blank=True, null=True, verbose_name='Number of Driver')
    isactive = models.SmallIntegerField(blank=True, null=True, verbose_name='Is Active')
    acc_user_location = models.CharField(max_length=120, blank=True, null=True, verbose_name='Account User Location')

    class Meta:
        managed = False
        db_table = 'acc_user'

    def __str__(self):
        return self.acc_user_id

    def get_absolute_url(self):
        return f'/{self.acc_user_id}/'  