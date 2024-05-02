# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DesignColumn(models.Model):
    row_guid = models.CharField(max_length=32, blank=True, null=True)
    column_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = '!_design_column'


class DesignComponent(models.Model):
    column_guid = models.ForeignKey(DesignColumn, models.DO_NOTHING, db_column='column_guid', blank=True, null=True)
    component_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    offset_cols_size = models.IntegerField(blank=True, null=True)
    offset_sm_size = models.IntegerField(blank=True, null=True)
    offset_md_size = models.IntegerField(blank=True, null=True)
    offset_lg_size = models.IntegerField(blank=True, null=True)
    offset_xl_size = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    input_type = models.CharField(max_length=100, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    left_label = models.CharField(max_length=100, blank=True, null=True)
    left_option_id = models.CharField(max_length=100, blank=True, null=True)
    left_option_url = models.CharField(max_length=200, blank=True, null=True)
    option_url = models.CharField(max_length=200, blank=True, null=True)
    dynamic = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = '!_design_component'


class DesignComponent20211112(models.Model):
    column_guid = models.CharField(max_length=32, blank=True, null=True)
    component_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    offset_cols_size = models.IntegerField(blank=True, null=True)
    offset_sm_size = models.IntegerField(blank=True, null=True)
    offset_md_size = models.IntegerField(blank=True, null=True)
    offset_lg_size = models.IntegerField(blank=True, null=True)
    offset_xl_size = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    input_type = models.CharField(max_length=100, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    left_label = models.CharField(max_length=100, blank=True, null=True)
    left_option_id = models.CharField(max_length=100, blank=True, null=True)
    left_option_url = models.CharField(max_length=200, blank=True, null=True)
    option_url = models.CharField(max_length=200, blank=True, null=True)
    dynamic = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = '!_design_component_20211112'


class DesignRow(models.Model):
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    row_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = '!_design_row'


class AccInternal(models.Model):
    trans_guid = models.CharField(primary_key=True, max_length=32)
    internal_name = models.CharField(max_length=60, blank=True, null=True)
    internal_url = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'acc_internal'


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
        managed =True
        db_table = 'acc_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed =True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed =True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed =True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed =True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed =True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed =True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed =True
        db_table = 'authtoken_token'


class CustomerProfile(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_regno = models.CharField(max_length=30, blank=True, null=True)
    customer_gstno = models.CharField(max_length=30, blank=True, null=True)
    customer_taxcode = models.CharField(max_length=30, blank=True, null=True)
    customer_add1 = models.CharField(max_length=60, blank=True, null=True)
    customer_add2 = models.CharField(max_length=60, blank=True, null=True)
    customer_add3 = models.CharField(max_length=60, blank=True, null=True)
    customer_add4 = models.CharField(max_length=60, blank=True, null=True)
    customer_postcode = models.CharField(max_length=6, blank=True, null=True)
    customer_state = models.CharField(max_length=20, blank=True, null=True)
    customer_country = models.CharField(max_length=25, blank=True, null=True)
    customer_tel = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'customer_profile'

class CustomerProfileTable(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_regno = models.CharField(max_length=30, blank=True, null=True)
    customer_gstno = models.CharField(max_length=30, blank=True, null=True)
    customer_taxcode = models.CharField(max_length=30, blank=True, null=True)
    customer_add1 = models.CharField(max_length=60, blank=True, null=True)
    customer_add2 = models.CharField(max_length=60, blank=True, null=True)
    customer_add3 = models.CharField(max_length=60, blank=True, null=True)
    customer_add4 = models.CharField(max_length=60, blank=True, null=True)
    customer_postcode = models.CharField(max_length=6, blank=True, null=True)
    customer_state = models.CharField(max_length=20, blank=True, null=True)
    customer_country = models.CharField(max_length=25, blank=True, null=True)
    customer_tel = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

class Meta:
        managed = False
        db_table = 'customer_profile'
        ordering = ('customer_name',)


class CustomerUrl(models.Model):
    url_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    customer_url = models.CharField(max_length=120, blank=True, null=True)
    key = models.CharField(max_length=60, blank=True, null=True)
    userid = models.CharField(max_length=32, blank=True, null=True)
    userpass = models.CharField(max_length=32, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'customer_url'


class DesignColumn(models.Model):
    row_guid = models.ForeignKey(DesignRow, models.DO_NOTHING, db_column='row_guid', blank=True, null=True)
    column_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_column'


class DesignComponent(models.Model):
    column_guid = models.ForeignKey(DesignColumn, models.DO_NOTHING, db_column='column_guid', blank=True, null=True)
    component_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    offset_cols_size = models.IntegerField(blank=True, null=True)
    offset_sm_size = models.IntegerField(blank=True, null=True)
    offset_md_size = models.IntegerField(blank=True, null=True)
    offset_lg_size = models.IntegerField(blank=True, null=True)
    offset_xl_size = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    input_type = models.CharField(max_length=100, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    left_label = models.CharField(max_length=100, blank=True, null=True)
    left_option_id = models.CharField(max_length=100, blank=True, null=True)
    left_option_url = models.CharField(max_length=200, blank=True, null=True)
    option_url = models.CharField(max_length=200, blank=True, null=True)
    dynamic = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_component'


class DesignComponent20211112(models.Model):
    column_guid = models.CharField(max_length=32, blank=True, null=True)
    component_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    offset_cols_size = models.IntegerField(blank=True, null=True)
    offset_sm_size = models.IntegerField(blank=True, null=True)
    offset_md_size = models.IntegerField(blank=True, null=True)
    offset_lg_size = models.IntegerField(blank=True, null=True)
    offset_xl_size = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    input_type = models.CharField(max_length=100, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    left_label = models.CharField(max_length=100, blank=True, null=True)
    left_option_id = models.CharField(max_length=100, blank=True, null=True)
    left_option_url = models.CharField(max_length=200, blank=True, null=True)
    option_url = models.CharField(max_length=200, blank=True, null=True)
    dynamic = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_component_20211112'


class DesignCot(models.Model):
    cot_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    tab_guid = models.CharField(max_length=32)
    cot_group = models.CharField(max_length=120, blank=True, null=True)
    cot_seq = models.SmallIntegerField(blank=True, null=True)
    cot_description = models.CharField(max_length=120, blank=True, null=True)
    cot_value = models.TextField(blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    isdeleted = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_cot'
        unique_together = (('cot_guid', 'customer_guid', 'tab_guid'),)


class DesignDynamic(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    tab_guid = models.ForeignKey('DesignTab', models.DO_NOTHING, db_column='tab_guid', blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    dynamic_seq = models.SmallIntegerField(blank=True, null=True)
    dynamic_value = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_dynamic'


class DesignDynamic20220221(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    dynamic_seq = models.SmallIntegerField(blank=True, null=True)
    dynamic_value = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_dynamic_20220221'


class DesignDynamicEverrise(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    dynamic_seq = models.SmallIntegerField(blank=True, null=True)
    dynamic_value = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_dynamic_everrise'


class DesignDynamicEverrisecanuse20220223(models.Model):
    dynamic_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    dynamic_seq = models.SmallIntegerField(blank=True, null=True)
    dynamic_value = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_dynamic_everriseCanUse_20220223'


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
        managed =True
        db_table = 'design_main_template'


class DesignMenu(models.Model):
    main_guid = models.ForeignKey(DesignMainTemplate, models.DO_NOTHING, db_column='main_guid', blank=True, null=True)
    design_menu_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_menu'


class DesignMenuChild(models.Model):
    design_menu_guid = models.ForeignKey(DesignMenu, models.DO_NOTHING, db_column='design_menu_guid', blank=True, null=True)
    design_menu_child_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_menu_child'


class DesignRow(models.Model):
    tab_guid = models.ForeignKey('DesignTab', models.DO_NOTHING, db_column='tab_guid', blank=True, null=True)
    row_guid = models.CharField(primary_key=True, max_length=32)
    seq = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_row'


class DesignTab(models.Model):
    template_guid = models.ForeignKey('DesignTemplate', models.DO_NOTHING, db_column='template_guid')
    tab_guid = models.CharField(primary_key=True, max_length=32)
    key_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'design_tab'


class DesignTemplate(models.Model):
    main_guid = models.ForeignKey(DesignMainTemplate, models.DO_NOTHING, db_column='main_guid', blank=True, null=True)
    template_guid = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=100, blank=True, null=True)
    json = models.JSONField(blank=True, null=True)
    line = models.CharField(max_length=6)

    class Meta:
        managed =True
        db_table = 'design_template'
        unique_together = (('template_guid', 'line'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed =True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed =True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed =True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed =True
        db_table = 'django_session'


class FormGroup(models.Model):
    form_guid = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=30)
    sequence = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'form_group'


class FormGroupC(models.Model):
    form_guid_c = models.CharField(primary_key=True, max_length=32)
    form_guid = models.ForeignKey(FormGroup, models.DO_NOTHING, db_column='form_guid', blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    key_table = models.CharField(max_length=32, blank=True, null=True)
    key_description = models.CharField(max_length=30, blank=True, null=True)
    default_description = models.CharField(max_length=60)
    input_type = models.CharField(max_length=60)
    input_default_value = models.CharField(max_length=60)
    input_option_type = models.CharField(max_length=32)
    input_value_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'form_group_c'


class FormGroupStatus(models.Model):
    status_key = models.CharField(primary_key=True, max_length=30)
    status_description = models.CharField(max_length=32, blank=True, null=True)
    status_process = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'form_group_status'


class FormOption(models.Model):
    option_guid = models.CharField(primary_key=True, max_length=32)
    option_type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'form_option'


class FormOptionValue(models.Model):
    option_guid = models.ForeignKey(FormOption, models.DO_NOTHING, db_column='option_guid', blank=True, null=True)
    option_child_guid = models.CharField(primary_key=True, max_length=32)
    option_type = models.CharField(max_length=100)
    option_seq = models.IntegerField(blank=True, null=True)
    option_value = models.TextField()
    option_description = models.TextField()
    option_default = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'form_option_value'


class MainFilter(models.Model):
    main_filter_guid = models.CharField(primary_key=True, max_length=32)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'main_filter'


class MainFilterChild(models.Model):
    main_filter_guid = models.ForeignKey(MainFilter, models.DO_NOTHING, db_column='main_filter_guid', blank=True, null=True)
    child_filter_guid = models.CharField(primary_key=True, max_length=32)
    cols_size = models.IntegerField(blank=True, null=True)
    sm_size = models.IntegerField(blank=True, null=True)
    md_size = models.IntegerField(blank=True, null=True)
    lg_size = models.IntegerField(blank=True, null=True)
    xl_size = models.IntegerField(blank=True, null=True)
    placeholder = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    parameter = models.CharField(max_length=100, blank=True, null=True)
    seq = models.SmallIntegerField(blank=True, null=True)
    option_type = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'main_filter_child'


class RimsAccCode(models.Model):
    acc_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    acc_type = models.CharField(max_length=32, blank=True, null=True)
    tta_field = models.CharField(max_length=32, blank=True, null=True)
    tta_description = models.CharField(max_length=60, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_acc_code'


class RimsAccGlmaster(models.Model):
    glmaster_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    acc_type = models.CharField(max_length=20, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    acc_description = models.CharField(max_length=60, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_acc_glmaster'
        unique_together = (('customer_guid', 'acc_code'),)


class RimsAccType(models.Model):
    acc_type_guid = models.CharField(primary_key=True, max_length=32)
    acc_type_code = models.CharField(max_length=20, blank=True, null=True)
    acc_type_description = models.CharField(max_length=60, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_acc_type'


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
        managed =True
        db_table = 'rims_banner'
        unique_together = (('banner_guid', 'customer_guid'),)


class RimsBrand(models.Model):
    brand_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    mcode = models.CharField(db_column='MCode', max_length=10)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'rims_brand'


class RimsCpSetBranch(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    branch_guid = models.CharField(db_column='BRANCH_GUID', max_length=32)  # Field name made lowercase.
    branch_code = models.CharField(db_column='BRANCH_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='BRANCH_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    branch_add = models.TextField(db_column='BRANCH_ADD', blank=True, null=True)  # Field name made lowercase.
    branch_tel = models.CharField(db_column='BRANCH_TEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branch_fax = models.CharField(db_column='BRANCH_FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    script_tablename = models.CharField(db_column='SCRIPT_TABLENAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set_ratio = models.FloatField(db_column='SET_RATIO', blank=True, null=True)  # Field name made lowercase.
    set_priority = models.IntegerField(db_column='SET_PRIORITY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set_supplier_code = models.CharField(db_column='SET_SUPPLIER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set_customer_code = models.CharField(db_column='SET_CUSTOMER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sshhostname = models.CharField(db_column='sshHostname', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sshport = models.IntegerField(db_column='sshPort', blank=True, null=True)  # Field name made lowercase.
    sshuser = models.CharField(db_column='sshUser', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sshpass = models.CharField(db_column='sshPass', max_length=30, blank=True, null=True)  # Field name made lowercase.
    databaset_default = models.CharField(max_length=50, blank=True, null=True)
    mysql_user = models.CharField(max_length=30, blank=True, null=True)
    mysql_pass = models.CharField(max_length=30, blank=True, null=True)
    sshcdesthost = models.CharField(db_column='sshCDestHost', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sshcdestport = models.IntegerField(db_column='sshCDestPort', blank=True, null=True)  # Field name made lowercase.
    sshcsourceport = models.IntegerField(db_column='sshCSourcePort', blank=True, null=True)  # Field name made lowercase.
    script_database_tablename = models.CharField(max_length=40, blank=True, null=True)
    outlet_code_acc = models.CharField(db_column='OUTLET_CODE_ACC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    periodendon = models.IntegerField(db_column='PeriodEndOn', blank=True, null=True)  # Field name made lowercase.
    lastrecaldatetime = models.DateTimeField(db_column='LastRecalDateTime', blank=True, null=True)  # Field name made lowercase.
    recaltime = models.TimeField(db_column='RecalTime', blank=True, null=True)  # Field name made lowercase.
    nontrade_as_stock = models.SmallIntegerField(blank=True, null=True)
    set_active = models.SmallIntegerField(blank=True, null=True)
    is_dc = models.SmallIntegerField(blank=True, null=True)
    rep_all_ads = models.SmallIntegerField(blank=True, null=True)
    branch_desc = models.CharField(max_length=20, blank=True, null=True)
    fifo_calc = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_cp_set_branch'
        unique_together = (('customer_guid', 'branch_guid'),)


class RimsCustomerData(models.Model):
    data_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    list_guid = models.CharField(max_length=32)
    module_type = models.CharField(max_length=60, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    data_json = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_customer_data'


class RimsDivDeptSdC(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    trans_guid = models.CharField(max_length=32)
    group_code = models.CharField(max_length=120, blank=True, null=True)
    group_desc = models.CharField(max_length=120, blank=True, null=True)
    dept = models.CharField(max_length=120, blank=True, null=True)
    dept_desc = models.CharField(max_length=120, blank=True, null=True)
    subdept = models.CharField(max_length=120, blank=True, null=True)
    subdeptdesc = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null=True)
    category_desc = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_div_dept_sd_c'
        unique_together = (('customer_guid', 'trans_guid'),)


class RimsPayTerm(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    code = models.CharField(db_column='Code', max_length=15)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.
    setactive = models.SmallIntegerField(db_column='SetActive', blank=True, null=True)  # Field name made lowercase.
    imported_at = models.DateTimeField(blank=True, null=True)
    sync_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_pay_term'
        unique_together = (('customer_guid', 'code'),)


class RimsPayTermChild(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    code = models.CharField(db_column='Code', max_length=15)  # Field name made lowercase.
    line = models.IntegerField()
    dayfrom = models.IntegerField(db_column='DayFrom', blank=True, null=True)  # Field name made lowercase.
    dayto = models.IntegerField(db_column='DayTo', blank=True, null=True)  # Field name made lowercase.
    paytype = models.CharField(db_column='PayType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    intervaldays = models.IntegerField(db_column='IntervalDays', blank=True, null=True)  # Field name made lowercase.
    intervalmonths = models.IntegerField(db_column='IntervalMonths', blank=True, null=True)  # Field name made lowercase.
    intervalweeks = models.IntegerField(db_column='IntervalWeeks', blank=True, null=True)  # Field name made lowercase.
    sub_code = models.CharField(max_length=15, blank=True, null=True)
    imported_at = models.DateTimeField(blank=True, null=True)
    sync_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_pay_term_child'
        unique_together = (('customer_guid', 'code', 'line'),)


class RimsSupcus(models.Model):
    customer_guid = models.CharField(max_length=32)
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add1 = models.CharField(db_column='Add1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add2 = models.CharField(db_column='Add2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add3 = models.CharField(db_column='Add3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=12, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymentday = models.IntegerField(db_column='PaymentDay', blank=True, null=True)  # Field name made lowercase.
    bankacc = models.CharField(db_column='BankAcc', max_length=35, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
    monitorcredit = models.SmallIntegerField(db_column='MonitorCredit', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    pointbf = models.FloatField(db_column='PointBF', blank=True, null=True)  # Field name made lowercase.
    pointcumm = models.FloatField(db_column='PointCumm', blank=True, null=True)  # Field name made lowercase.
    pointsum = models.FloatField(db_column='PointSum', blank=True, null=True)  # Field name made lowercase.
    member = models.SmallIntegerField(db_column='Member', blank=True, null=True)  # Field name made lowercase.
    memberno = models.CharField(max_length=20, blank=True, null=True)
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cyclevisit = models.IntegerField(db_column='CycleVisit', blank=True, null=True)  # Field name made lowercase.
    deliveryterm = models.IntegerField(blank=True, null=True)
    issuedstamp = models.DateTimeField(db_column='IssuedStamp', blank=True, null=True)  # Field name made lowercase.
    laststamp = models.DateTimeField(db_column='LastStamp', blank=True, null=True)  # Field name made lowercase.
    dadd1 = models.CharField(max_length=60, blank=True, null=True)
    dadd2 = models.CharField(max_length=60, blank=True, null=True)
    dadd3 = models.CharField(max_length=60, blank=True, null=True)
    dattn = models.CharField(max_length=60, blank=True, null=True)
    dtel = models.CharField(max_length=20, blank=True, null=True)
    dfax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    accountcode = models.CharField(db_column='AccountCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accpdebit = models.CharField(db_column='AccPDebit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accpcredit = models.CharField(db_column='AccPCredit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    calduedateby = models.CharField(db_column='CalDueDateby', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supcusgroup = models.CharField(db_column='supcusGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=10, blank=True, null=True)
    pcode = models.CharField(max_length=10, blank=True, null=True)
    add4 = models.CharField(db_column='Add4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    contact2 = models.CharField(db_column='Contact2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dadd4 = models.CharField(db_column='DAdd4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    poprice_method = models.CharField(max_length=10, blank=True, null=True)
    stockday_min = models.FloatField(blank=True, null=True)
    stockday_max = models.FloatField(blank=True, null=True)
    stock_returnable = models.FloatField(blank=True, null=True)
    stock_return_cost_type = models.CharField(max_length=10, blank=True, null=True)
    autoclosepo = models.SmallIntegerField(db_column='AutoClosePO', blank=True, null=True)  # Field name made lowercase.
    consign = models.SmallIntegerField(db_column='Consign', blank=True, null=True)  # Field name made lowercase.
    block = models.SmallIntegerField(db_column='Block', blank=True, null=True)  # Field name made lowercase.
    exclude_orderqty_control = models.SmallIntegerField(blank=True, null=True)
    supcus_guid = models.CharField(primary_key=True, max_length=32)
    acc_no = models.CharField(max_length=20, blank=True, null=True)
    ord_w1 = models.SmallIntegerField(db_column='Ord_W1', blank=True, null=True)  # Field name made lowercase.
    ord_w2 = models.SmallIntegerField(db_column='Ord_W2', blank=True, null=True)  # Field name made lowercase.
    ord_w3 = models.SmallIntegerField(db_column='Ord_W3', blank=True, null=True)  # Field name made lowercase.
    ord_w4 = models.SmallIntegerField(db_column='Ord_W4', blank=True, null=True)  # Field name made lowercase.
    ord_d1 = models.SmallIntegerField(db_column='Ord_D1', blank=True, null=True)  # Field name made lowercase.
    ord_d2 = models.SmallIntegerField(db_column='Ord_D2', blank=True, null=True)  # Field name made lowercase.
    ord_d3 = models.SmallIntegerField(db_column='Ord_D3', blank=True, null=True)  # Field name made lowercase.
    ord_d4 = models.SmallIntegerField(db_column='Ord_D4', blank=True, null=True)  # Field name made lowercase.
    ord_d5 = models.SmallIntegerField(db_column='Ord_D5', blank=True, null=True)  # Field name made lowercase.
    ord_d6 = models.SmallIntegerField(db_column='Ord_D6', blank=True, null=True)  # Field name made lowercase.
    ord_d7 = models.SmallIntegerField(db_column='Ord_D7', blank=True, null=True)  # Field name made lowercase.
    rec_method_1 = models.SmallIntegerField(db_column='Rec_Method_1', blank=True, null=True)  # Field name made lowercase.
    rec_method_2 = models.SmallIntegerField(db_column='Rec_Method_2', blank=True, null=True)  # Field name made lowercase.
    rec_method_3 = models.SmallIntegerField(db_column='Rec_Method_3', blank=True, null=True)  # Field name made lowercase.
    rec_method_4 = models.SmallIntegerField(db_column='Rec_Method_4', blank=True, null=True)  # Field name made lowercase.
    rec_method_5 = models.SmallIntegerField(db_column='Rec_Method_5', blank=True, null=True)  # Field name made lowercase.
    pur_expiry_days = models.IntegerField(blank=True, null=True)
    grn_baseon_pocost = models.SmallIntegerField(blank=True, null=True)
    ord_set_global = models.SmallIntegerField(db_column='Ord_set_global', blank=True, null=True)  # Field name made lowercase.
    rules_code = models.CharField(max_length=20, blank=True, null=True)
    po_negative_qty = models.SmallIntegerField(blank=True, null=True)
    grpo_variance_qty = models.FloatField(blank=True, null=True)
    grpo_variance_price = models.FloatField(blank=True, null=True)
    price_include_tax = models.SmallIntegerField(blank=True, null=True)
    delivery_early_in_day = models.IntegerField(blank=True, null=True)
    delivery_late_in_day = models.IntegerField(blank=True, null=True)
    tax_code = models.CharField(max_length=10, blank=True, null=True)
    gst_start_date = models.DateField(blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    reg_no = models.CharField(max_length=25, blank=True, null=True)
    name_reg = models.CharField(max_length=80, blank=True, null=True)
    multi_tax_rate = models.SmallIntegerField(blank=True, null=True)
    grn_allow_negative_margin = models.SmallIntegerField(blank=True, null=True)
    rebate_as_inv = models.SmallIntegerField(blank=True, null=True)
    discount_as_inv = models.SmallIntegerField(blank=True, null=True)
    poso_line_max = models.IntegerField(blank=True, null=True)
    apply_actual_cn = models.SmallIntegerField(blank=True, null=True)
    promorebateastaxinv = models.SmallIntegerField(db_column='PromoRebateAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    purchasednamtastaxinv = models.SmallIntegerField(db_column='PurchaseDNAmtAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    member_accno = models.CharField(max_length=20, blank=True, null=True)
    roundingadjust = models.SmallIntegerField(db_column='RoundingAdjust', blank=True, null=True)  # Field name made lowercase.
    mobile_po = models.SmallIntegerField(blank=True, null=True)
    auto_grn_mobile_po = models.SmallIntegerField(blank=True, null=True)
    min_expiry_day = models.SmallIntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=5, blank=True, null=True)
    sstregno = models.CharField(db_column='SSTRegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssteffectivedate = models.DateField(db_column='SSTEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    sstdefaultcode = models.CharField(db_column='SSTDefaultCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sstdefaulttaxintno = models.IntegerField(db_column='SSTDefaultTaxIntNo', blank=True, null=True)  # Field name made lowercase.
    replenish_date = models.CharField(max_length=12, blank=True, null=True)
    replenish_stockbalance = models.SmallIntegerField(blank=True, null=True)
    b2b_registration = models.SmallIntegerField(blank=True, null=True)
    cdi = models.SmallIntegerField(blank=True, null=True)
    cpm = models.SmallIntegerField(blank=True, null=True)
    auto_price_change = models.SmallIntegerField(blank=True, null=True)
    promo_date = models.SmallIntegerField(blank=True, null=True)
    pos_sales = models.SmallIntegerField(blank=True, null=True)
    sales_agent = models.CharField(max_length=30, blank=True, null=True)
    stk_rtn_collect_day = models.SmallIntegerField(blank=True, null=True)
    imported_at = models.DateTimeField(blank=True, null=True)
    sync_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_supcus'


class RimsSupcusLink(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    link_guid = models.CharField(max_length=32)
    supcus_guid = models.CharField(max_length=32, blank=True, null=True)
    selected_guid = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    imported_at = models.DateTimeField(blank=True, null=True)
    sync_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'rims_supcus_link'
        unique_together = (('customer_guid', 'link_guid'),)


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
        managed =True
        db_table = 'set_user'
        unique_together = (('user_guid', 'customer_guid'),)


class Supcus(models.Model):
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    code = models.CharField(db_column='Code', primary_key=True, max_length=15)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add1 = models.CharField(db_column='Add1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add2 = models.CharField(db_column='Add2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    add3 = models.CharField(db_column='Add3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=25, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=60, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymentday = models.IntegerField(db_column='PaymentDay', blank=True, null=True)  # Field name made lowercase.
    bankacc = models.CharField(db_column='BankAcc', max_length=35, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
    monitorcredit = models.SmallIntegerField(db_column='MonitorCredit', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    pointbf = models.FloatField(db_column='PointBF', blank=True, null=True)  # Field name made lowercase.
    pointcumm = models.FloatField(db_column='PointCumm', blank=True, null=True)  # Field name made lowercase.
    pointsum = models.FloatField(db_column='PointSum', blank=True, null=True)  # Field name made lowercase.
    member = models.SmallIntegerField(db_column='Member', blank=True, null=True)  # Field name made lowercase.
    memberno = models.CharField(max_length=20, blank=True, null=True)
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    cyclevisit = models.IntegerField(db_column='CycleVisit', blank=True, null=True)  # Field name made lowercase.
    deliveryterm = models.IntegerField(db_column='DeliveryTerm', blank=True, null=True)  # Field name made lowercase.
    issuedstamp = models.DateTimeField(db_column='IssuedStamp', blank=True, null=True)  # Field name made lowercase.
    laststamp = models.DateTimeField(db_column='LastStamp', blank=True, null=True)  # Field name made lowercase.
    dadd1 = models.CharField(max_length=60, blank=True, null=True)
    dadd2 = models.CharField(max_length=60, blank=True, null=True)
    dadd3 = models.CharField(max_length=60, blank=True, null=True)
    dattn = models.CharField(max_length=60, blank=True, null=True)
    dtel = models.CharField(max_length=30, blank=True, null=True)
    dfax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    accountcode = models.CharField(db_column='AccountCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accpdebit = models.CharField(db_column='AccPDebit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accpcredit = models.CharField(db_column='AccPCredit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    calduedateby = models.CharField(db_column='CalDueDateby', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supcusgroup = models.CharField(db_column='supcusGroup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=10, blank=True, null=True)
    pcode = models.CharField(max_length=10, blank=True, null=True)
    add4 = models.CharField(db_column='Add4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    contact2 = models.CharField(db_column='Contact2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dadd4 = models.CharField(db_column='DAdd4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    poprice_method = models.CharField(max_length=10, blank=True, null=True)
    stockday_min = models.FloatField(blank=True, null=True)
    stockday_max = models.FloatField(blank=True, null=True)
    stock_returnable = models.FloatField(blank=True, null=True)
    stock_return_cost_type = models.CharField(max_length=10, blank=True, null=True)
    autoclosepo = models.SmallIntegerField(db_column='AutoClosePO', blank=True, null=True)  # Field name made lowercase.
    consign = models.SmallIntegerField(db_column='Consign', blank=True, null=True)  # Field name made lowercase.
    block = models.SmallIntegerField(db_column='Block', blank=True, null=True)  # Field name made lowercase.
    exclude_orderqty_control = models.SmallIntegerField(blank=True, null=True)
    supcus_guid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    acc_no = models.CharField(max_length=20, blank=True, null=True)
    ord_w1 = models.SmallIntegerField(db_column='Ord_W1', blank=True, null=True)  # Field name made lowercase.
    ord_w2 = models.SmallIntegerField(db_column='Ord_W2', blank=True, null=True)  # Field name made lowercase.
    ord_w3 = models.SmallIntegerField(db_column='Ord_W3', blank=True, null=True)  # Field name made lowercase.
    ord_w4 = models.SmallIntegerField(db_column='Ord_W4', blank=True, null=True)  # Field name made lowercase.
    ord_d1 = models.SmallIntegerField(db_column='Ord_D1', blank=True, null=True)  # Field name made lowercase.
    ord_d2 = models.SmallIntegerField(db_column='Ord_D2', blank=True, null=True)  # Field name made lowercase.
    ord_d3 = models.SmallIntegerField(db_column='Ord_D3', blank=True, null=True)  # Field name made lowercase.
    ord_d4 = models.SmallIntegerField(db_column='Ord_D4', blank=True, null=True)  # Field name made lowercase.
    ord_d5 = models.SmallIntegerField(db_column='Ord_D5', blank=True, null=True)  # Field name made lowercase.
    ord_d6 = models.SmallIntegerField(db_column='Ord_D6', blank=True, null=True)  # Field name made lowercase.
    ord_d7 = models.SmallIntegerField(db_column='Ord_D7', blank=True, null=True)  # Field name made lowercase.
    rec_method_1 = models.SmallIntegerField(db_column='Rec_Method_1', blank=True, null=True)  # Field name made lowercase.
    rec_method_2 = models.SmallIntegerField(db_column='Rec_Method_2', blank=True, null=True)  # Field name made lowercase.
    rec_method_3 = models.SmallIntegerField(db_column='Rec_Method_3', blank=True, null=True)  # Field name made lowercase.
    rec_method_4 = models.SmallIntegerField(db_column='Rec_Method_4', blank=True, null=True)  # Field name made lowercase.
    rec_method_5 = models.SmallIntegerField(db_column='Rec_Method_5', blank=True, null=True)  # Field name made lowercase.
    pur_expiry_days = models.IntegerField(blank=True, null=True)
    grn_baseon_pocost = models.SmallIntegerField(blank=True, null=True)
    ord_set_global = models.SmallIntegerField(db_column='Ord_set_global', blank=True, null=True)  # Field name made lowercase.
    rules_code = models.CharField(max_length=20, blank=True, null=True)
    po_negative_qty = models.SmallIntegerField(blank=True, null=True)
    grpo_variance_qty = models.FloatField(blank=True, null=True)
    grpo_variance_price = models.FloatField(blank=True, null=True)
    price_include_tax = models.SmallIntegerField(blank=True, null=True)
    delivery_early_in_day = models.IntegerField(blank=True, null=True)
    delivery_late_in_day = models.IntegerField(blank=True, null=True)
    tax_code = models.CharField(max_length=10, blank=True, null=True)
    gst_start_date = models.DateField(blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    reg_no = models.CharField(max_length=25, blank=True, null=True)
    name_reg = models.CharField(max_length=80, blank=True, null=True)
    multi_tax_rate = models.SmallIntegerField(blank=True, null=True)
    grn_allow_negative_margin = models.SmallIntegerField(blank=True, null=True)
    rebate_as_inv = models.SmallIntegerField(blank=True, null=True)
    discount_as_inv = models.SmallIntegerField(blank=True, null=True)
    poso_line_max = models.IntegerField(blank=True, null=True)
    apply_actual_cn = models.SmallIntegerField(blank=True, null=True)
    purchasednamtastaxinv = models.SmallIntegerField(db_column='PurchaseDNAmtAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    member_accno = models.CharField(max_length=20, blank=True, null=True)
    promorebateastaxinv = models.SmallIntegerField(db_column='PromoRebateAsTaxInv', blank=True, null=True)  # Field name made lowercase.
    roundingadjust = models.SmallIntegerField(db_column='RoundingAdjust', blank=True, null=True)  # Field name made lowercase.
    mobile_po = models.SmallIntegerField(blank=True, null=True)
    auto_grn_mobile_po = models.SmallIntegerField(blank=True, null=True)
    min_expiry_day = models.SmallIntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=5, blank=True, null=True)
    sstregno = models.CharField(db_column='SSTRegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssteffectivedate = models.DateField(db_column='SSTEffectiveDate', blank=True, null=True)  # Field name made lowercase.
    sstdefaultcode = models.CharField(db_column='SSTDefaultCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sstdefaulttaxintno = models.IntegerField(db_column='SSTDefaultTaxIntNo', blank=True, null=True)  # Field name made lowercase.
    replenish_date = models.CharField(max_length=12, blank=True, null=True)
    replenish_stockbalance = models.SmallIntegerField(blank=True, null=True)
    b2b_registration = models.SmallIntegerField(blank=True, null=True)
    cdi = models.SmallIntegerField(blank=True, null=True)
    cpm = models.SmallIntegerField(blank=True, null=True)
    auto_price_change = models.SmallIntegerField(blank=True, null=True)
    promo_date = models.SmallIntegerField(blank=True, null=True)
    pos_sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'supcus'


class Sysrun(models.Model):
    customer_guid = models.CharField(unique=True, max_length=32)
    customer_prefix = models.CharField(max_length=5)
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    code = models.CharField(max_length=10)
    currentno = models.IntegerField(db_column='CurrentNo', blank=True, null=True)  # Field name made lowercase.
    nodigit = models.IntegerField(db_column='NoDigit', blank=True, null=True)  # Field name made lowercase.
    yyyy = models.IntegerField(db_column='YYYY', blank=True, null=True)  # Field name made lowercase.
    mm = models.IntegerField(db_column='MM', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =True
        db_table = 'sysrun'


class TemplateCopy(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    description = models.CharField(max_length=100, blank=True, null=True)
    json = models.JSONField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'template_copy'


class TtaList(models.Model):
    list_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    refno = models.CharField(max_length=20)
    supplier_guid = models.CharField(max_length=32)
    supplier_code = models.CharField(max_length=15, blank=True, null=True)
    supplier_name = models.CharField(max_length=60, blank=True, null=True)
    bill_supp_guid = models.CharField(max_length=32, blank=True, null=True)
    bill_supp_code = models.CharField(max_length=15, blank=True, null=True)
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True)
    negotiation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    co_reg_no = models.CharField(max_length=32, blank=True, null=True)
    tta_period_from = models.CharField(max_length=32, blank=True, null=True)
    tta_period_to = models.CharField(max_length=32, blank=True, null=True)
    internal_pic = models.CharField(max_length=60, blank=True, null=True)
    trading_group = models.CharField(max_length=60, blank=True, null=True)
    trading_type = models.CharField(max_length=60, blank=True, null=True)
    delivery_mode = models.CharField(max_length=60, blank=True, null=True)
    returnable = models.CharField(max_length=10, blank=True, null=True)
    supplier_pic = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_name = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_position = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_contact = models.CharField(max_length=60, blank=True, null=True)
    supplier_pic_email = models.CharField(max_length=60, blank=True, null=True)
    banner = models.TextField(blank=True, null=True)
    outlet = models.TextField(blank=True, null=True)
    supplier_profile = models.JSONField(blank=True, null=True)
    purchase_n_rebates = models.JSONField(blank=True, null=True)
    payment_n_discount = models.JSONField(blank=True, null=True)
    stock_n_deliveries = models.JSONField(blank=True, null=True)
    administration_fees = models.JSONField(blank=True, null=True)
    business_growth_support = models.JSONField(blank=True, null=True)
    promotion_support = models.JSONField(blank=True, null=True)
    display_incentive = models.JSONField(blank=True, null=True)
    marketing_support = models.JSONField(blank=True, null=True)
    e_commerce_support = models.JSONField(blank=True, null=True)
    concess_n_consign = models.JSONField(blank=True, null=True)
    data_sharing_plan = models.JSONField(blank=True, null=True)
    condition_of_trade = models.JSONField(blank=True, null=True)
    effective_date = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    submit_by = models.CharField(max_length=100, blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    approve_by = models.CharField(max_length=100, blank=True, null=True)
    reject_at = models.DateTimeField(blank=True, null=True)
    reject_by = models.CharField(max_length=100, blank=True, null=True)
    list_status = models.CharField(max_length=20, blank=True, null=True)
    ecommerce_support = models.JSONField(blank=True, null=True)
    purchase_rebate_tier = models.JSONField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list'

class TtaListDetails(models.Model):
    list_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    refno = models.CharField(max_length=20)
    supplier_guid = models.CharField(max_length=32)
    supplier_name = models.CharField(max_length=60, blank=True, null=True)
    bill_supp_guid = models.CharField(max_length=32)
    bill_supp_name = models.CharField(max_length=60, blank=True, null=True)
    negotiation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    co_reg_no = models.IntegerField(blank=True, null=True)
    tta_period_from = models.CharField(max_length=200, blank=True, null=True)
    tta_period_to = models.CharField(max_length=200, blank=True, null=True)
    internal_pic = models.CharField(max_length=200, blank=True, null=True)
    trading_group = models.CharField(max_length=200, blank=True, null=True)
    trading_type = models.CharField(max_length=200, blank=True, null=True)
    delivery_mode = models.CharField(max_length=200, blank=True, null=True)
    returnable = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_name = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_position = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_contact = models.CharField(max_length=200, blank=True, null=True)
    supplier_pic_email = models.CharField(max_length=200, blank=True, null=True)
    banner = models.CharField(max_length=200, blank=True, null=True)
    outlet = models.CharField(max_length=200, blank=True, null=True)
    target_purchase_per_year_left_option = models.CharField(max_length=200, blank=True, null=True)
    target_purchase_per_year = models.IntegerField(blank=True, null=True)
    target_purchase_per_year_option = models.CharField(max_length=200, blank=True, null=True)
    flat_rebate_left_option = models.CharField(max_length=200, blank=True, null=True)
    flat_rebate = models.IntegerField(blank=True, null=True)
    flat_rebate_option = models.CharField(max_length=200, blank=True, null=True)
    business_development_fund_left_option = models.CharField(max_length=200, blank=True, null=True)
    business_development_fund = models.IntegerField(blank=True, null=True)
    business_development_fund_option = models.CharField(max_length=200, blank=True, null=True)
    payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True)
    payment_terms = models.CharField(max_length=200, blank=True, null=True)
    early_payment_terms_left_option = models.CharField(max_length=200, blank=True, null=True)
    early_payment_terms = models.CharField(max_length=200, blank=True, null=True)
    early_payment_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    early_payment_discount = models.IntegerField(blank=True, null=True)
    early_payment_discount_option = models.CharField(max_length=200, blank=True, null=True)
    cross_docking_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    cross_docking_allowance = models.IntegerField(blank=True, null=True)
    cross_docking_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    east_malaysia_orders_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    east_malaysia_orders_allowance = models.IntegerField(blank=True, null=True)
    east_malaysia_orders_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    damage_good_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    damage_good_allowance = models.IntegerField(blank=True, null=True)
    damage_good_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    non_compliance_packaging_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    non_compliance_packaging_allowance = models.IntegerField(blank=True, null=True)
    non_compliance_packaging_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_fulfillment_left_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_fulfillment = models.IntegerField(blank=True, null=True)
    purchase_order_fulfillment_option = models.CharField(max_length=200, blank=True, null=True)
    unfulfilled_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    unfulfilled_penalty = models.IntegerField(blank=True, null=True)
    unfulfilled_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    lost_of_profit_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    lost_of_profit_penalty = models.IntegerField(blank=True, null=True)
    lost_of_profit_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time_left_option = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time = models.CharField(max_length=200, blank=True, null=True)
    purchase_order_lead_time_option = models.CharField(max_length=200, blank=True, null=True)
    lead_time_penalty_left_option = models.CharField(max_length=200, blank=True, null=True)
    lead_time_penalty = models.IntegerField(blank=True, null=True)
    lead_time_penalty_option = models.CharField(max_length=200, blank=True, null=True)
    account_administration_fee_left_option = models.CharField(max_length=200, blank=True, null=True)
    account_administration_fee = models.IntegerField(blank=True, null=True)
    account_administration_fee_option = models.CharField(max_length=200, blank=True, null=True)
    product_registration_fee_left_option = models.CharField(max_length=200, blank=True, null=True)
    product_registration_fee = models.IntegerField(blank=True, null=True)
    product_registration_fee_option = models.CharField(max_length=200, blank=True, null=True)
    sku_replacement_left_option = models.CharField(max_length=200, blank=True, null=True)
    sku_replacement = models.IntegerField(blank=True, null=True)
    sku_replacement_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing = models.CharField(max_length=200, blank=True, null=True)
    new_item_listing_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_item_first_order_discount_2 = models.IntegerField(blank=True, null=True)
    new_item_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_opening_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_opening = models.IntegerField(blank=True, null=True)
    new_store_opening_option = models.CharField(max_length=200, blank=True, null=True)
    refurbish_store_left_option = models.CharField(max_length=200, blank=True, null=True)
    refurbish_store = models.IntegerField(blank=True, null=True)
    refurbish_store_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_allowance_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_allowance = models.IntegerField(blank=True, null=True)
    anniversary_sales_allowance_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_orders_rebate_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_orders_rebate = models.IntegerField(blank=True, null=True)
    anniversary_orders_rebate_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_2_left_option = models.CharField(max_length=200, blank=True, null=True)
    new_store_first_order_discount_2 = models.IntegerField(blank=True, null=True)
    new_store_first_order_discount_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    anniversary_sales = models.IntegerField(blank=True, null=True)
    anniversary_sales_option = models.CharField(max_length=200, blank=True, null=True)
    chinese_new_year_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    chinese_new_year_sales = models.IntegerField(blank=True, null=True)
    chinese_new_year_sales_option = models.CharField(max_length=200, blank=True, null=True)
    hari_raya_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    hari_raya_sales = models.IntegerField(blank=True, null=True)
    hari_raya_sales_option = models.CharField(max_length=200, blank=True, null=True)
    christmas_sales_left_option = models.CharField(max_length=200, blank=True, null=True)
    christmas_sales = models.IntegerField(blank=True, null=True)
    christmas_sales_option = models.CharField(max_length=200, blank=True, null=True)
    in_store_display_left_option = models.CharField(max_length=200, blank=True, null=True)
    in_store_display = models.IntegerField(blank=True, null=True)
    in_store_display_option = models.CharField(max_length=200, blank=True, null=True)
    press_advertisement_n_mailer_left_option = models.CharField(max_length=200, blank=True, null=True)
    press_advertisement_n_mailer = models.IntegerField(blank=True, null=True)
    press_advertisement_n_mailer_option = models.CharField(max_length=200, blank=True, null=True)
    adhoc_support_left_option = models.CharField(max_length=200, blank=True, null=True)
    adhoc_support = models.IntegerField(blank=True, null=True)
    adhoc_support_option = models.CharField(max_length=200, blank=True, null=True)
    crm_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    crm_event = models.IntegerField(blank=True, null=True)
    crm_event_option = models.CharField(max_length=200, blank=True, null=True)
    marketing_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    marketing_event = models.IntegerField(blank=True, null=True)
    marketing_event_option = models.CharField(max_length=200, blank=True, null=True)
    concourse_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    concourse_event = models.IntegerField(blank=True, null=True)
    concourse_event_option = models.CharField(max_length=200, blank=True, null=True)
    system_setup_n_maintenance_left_option = models.CharField(max_length=200, blank=True, null=True)
    system_setup_n_maintenance = models.IntegerField(blank=True, null=True)
    system_setup_n_maintenance_option = models.CharField(max_length=200, blank=True, null=True)
    digital_communication_left_option = models.CharField(max_length=200, blank=True, null=True)
    digital_communication = models.IntegerField(blank=True, null=True)
    digital_communication_option = models.CharField(max_length=200, blank=True, null=True)
    social_media_post_left_option = models.CharField(max_length=200, blank=True, null=True)
    social_media_post = models.IntegerField(blank=True, null=True)
    social_media_post_option = models.CharField(max_length=200, blank=True, null=True)
    market_place_event_left_option = models.CharField(max_length=200, blank=True, null=True)
    market_place_event = models.IntegerField(blank=True, null=True)
    market_place_event_option = models.CharField(max_length=200, blank=True, null=True)
    normal_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    normal_items = models.IntegerField(blank=True, null=True)
    normal_items_option = models.CharField(max_length=200, blank=True, null=True)
    best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    best_buy_items = models.IntegerField(blank=True, null=True)
    best_buy_items_option = models.CharField(max_length=200, blank=True, null=True)
    super_best_buy_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    super_best_buy_items = models.IntegerField(blank=True, null=True)
    super_best_buy_items_option = models.CharField(max_length=200, blank=True, null=True)
    mark_down_items_left_option = models.CharField(max_length=200, blank=True, null=True)
    mark_down_items = models.IntegerField(blank=True, null=True)
    mark_down_items_option = models.CharField(max_length=200, blank=True, null=True)
    number_50_percent_discount_left_option = models.CharField(db_column='50_percent_discount_left_option', max_length=200, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50_percent_discount = models.IntegerField(db_column='50_percent_discount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50_percent_discount_option = models.CharField(db_column='50_percent_discount_option', max_length=200, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    data_sharing_subscription_left_option = models.CharField(max_length=200, blank=True, null=True)
    data_sharing_subscription = models.IntegerField(blank=True, null=True)
    data_sharing_subscription_option = models.CharField(max_length=200, blank=True, null=True)
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True)
    weekly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True)
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf = models.CharField(max_length=200, blank=True, null=True)
    monthly_sales_n_qty_perf_by_store_vs_lst_year_perf_option = models.CharField(max_length=200, blank=True, null=True)
    weekly_stock_listing_by_sku = models.CharField(max_length=200, blank=True, null=True)
    weekly_stock_listing_by_sku_option = models.CharField(max_length=200, blank=True, null=True)
    general_complicance = models.CharField(max_length=200, blank=True, null=True)
    return_condition = models.CharField(max_length=200, blank=True, null=True)
    price_n_billing = models.CharField(max_length=200, blank=True, null=True)
    effective_date = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    submit_by = models.CharField(max_length=20, blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    approve_by = models.CharField(max_length=20, blank=True, null=True)
    reject_at = models.DateTimeField(blank=True, null=True)
    reject_by = models.CharField(max_length=20, blank=True, null=True)
    list_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tta_list'
        ordering = ('refno',)

class TtaListCal(models.Model):
    cal_guid = models.CharField(max_length=32, blank=True, null=True)
    list_guid = models.CharField(max_length=32, blank=True, null=True)
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    calmethod = models.CharField(db_column='calMethod', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calfield = models.CharField(db_column='calField', max_length=32, blank=True, null=True)  # Field name made lowercase.
    calunit = models.CharField(db_column='calUnit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    calvalue = models.DecimalField(db_column='calValue', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valinput1 = models.DecimalField(db_column='valInput1', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valinput2 = models.DecimalField(db_column='valInput2', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valinput3 = models.DecimalField(db_column='valInput3', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valinput4 = models.DecimalField(db_column='valInput4', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valcal1 = models.DecimalField(db_column='valCal1', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valcal2 = models.DecimalField(db_column='valCal2', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valcal3 = models.DecimalField(db_column='valCal3', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    valcal4 = models.DecimalField(db_column='valCal4', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list_cal'


class TtaListCalMain(models.Model):
    cal_guid = models.CharField(primary_key=True, max_length=32)
    tta_list_guid = models.CharField(max_length=32)
    loc_group = models.CharField(max_length=32)
    sup_code = models.CharField(max_length=20, blank=True, null=True)
    sup_name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    brand_desc = models.CharField(max_length=100, blank=True, null=True)
    gr_amt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    gr_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debitamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    creditamt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    credit_surchg = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    pdnamt = models.DecimalField(db_column='PDNamt', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pcnamt = models.DecimalField(db_column='PCNamt', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list_cal_main'


class TtaListForm(models.Model):
    list_guid_c = models.CharField(primary_key=True, max_length=32)
    list_guid = models.ForeignKey(TtaList, models.DO_NOTHING, db_column='list_guid', blank=True, null=True)
    tab_guid = models.CharField(max_length=32, blank=True, null=True)
    group = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    key_description = models.CharField(max_length=100, blank=True, null=True)
    left_option = models.CharField(max_length=100, blank=True, null=True)
    varchar_1 = models.CharField(max_length=120, blank=True, null=True)
    type_1 = models.CharField(max_length=32, blank=True, null=True)
    val_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    text_1 = models.TextField(blank=True, null=True)
    type_2 = models.CharField(max_length=32, blank=True, null=True)
    val_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    type_3 = models.CharField(max_length=32, blank=True, null=True)
    val_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list_form'


class TtaListStatus(models.Model):
    status_key = models.CharField(primary_key=True, max_length=30)
    status_description = models.CharField(max_length=32, blank=True, null=True)
    status_process = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list_status'


class TtaListStatusTrans(models.Model):
    customer_guid = models.CharField(max_length=32, blank=True, null=True)
    list_guid = models.CharField(max_length=32, blank=True, null=True)
    trans_guid = models.CharField(primary_key=True, max_length=32)
    status_key = models.CharField(max_length=30, blank=True, null=True)
    status_description = models.CharField(max_length=32, blank=True, null=True)
    status_process = models.CharField(max_length=60, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_list_status_trans'


class TtaLogs(models.Model):
    log_guid = models.CharField(primary_key=True, max_length=32)
    customer_guid = models.CharField(max_length=32)
    log_module = models.CharField(max_length=255, blank=True, null=True)
    log_ref = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=60, blank=True, null=True)
    log_json = models.JSONField(blank=True, null=True)
    remark = models.JSONField(blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'tta_logs'
