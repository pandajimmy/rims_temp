from django.db import models
from _mc_get_customer_profile.models import CustomerProfile

class SetUser(models.Model):
    customer_guid = models.OneToOneField(CustomerProfile, on_delete=models.DO_NOTHING, db_column='customer_guid', verbose_name='Customer guid', related_name='set_user_customer_profile')
    loc_count = models.SmallIntegerField(blank=True, null=True, verbose_name='Count of Location')
    loc_group = models.CharField(max_length=32, blank=True, null=True, verbose_name='Group of Location')
    user_group_guid = models.CharField(max_length=32, blank=True, null=True, verbose_name='User Group guid')
    user_group_name = models.CharField(max_length=120, blank=True, null=True, verbose_name='User Group Name')
    user_guid = models.CharField(primary_key=True, max_length=32, verbose_name='User guid')
    user_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='User Identifier')
    user_password = models.CharField(max_length=15, blank=True, null=True, verbose_name='User Password')
    user_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='User Name')
    user_email = models.CharField(max_length=100, blank=True, null=True, verbose_name='User Email')
    user_instance = models.CharField(max_length=120, blank=True, null=True, verbose_name='User Instance')
    user_instance_variable = models.CharField(max_length=120, blank=True, null=True, verbose_name='User Instance Variable')
    isactive = models.IntegerField(blank=True, null=True, verbose_name='Is Active')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created at')
    created_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='Created by')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Updated at')
    updated_by = models.CharField(max_length=255, blank=True, null=True, verbose_name='Updated by')
    mobile_status = models.IntegerField(blank=True, null=True, verbose_name='Mobile Status')

    class Meta:
        managed = False
        db_table = 'set_user'
        unique_together = (('user_guid', 'customer_guid'),)
        ordering = ('user_id',)

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return f'/{self.user_id}/'  