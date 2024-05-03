"""backend_rims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from nav_list import views

# Define the list of endpoints you want to show in mc
mc_included_endpoints = [
path('mc_design_template/', include('_mc_design_template.urls')),
    path('mc_design_tab/', include('_mc_design_tab.urls')),
    #path('mc_design_row/', include('_mc_design_row.urls')),
    #path('mc_design_column/', include('_mc_design_column.urls')),
    path('mc_design_component/', include('_mc_design_component.urls')),
    #path('mc_supcus/', include('_mc_supcus.urls')),
    #path('mc_form_option/', include('_mc_form_option.urls')),
    #path('mc_form_option_value/', include('_mc_form_option_value.urls')),
    path('mc_main_filter/', include('_mc_main_filter.urls')),
    path('mc_main_filter_child/', include('_mc_main_filter_child.urls')),
    path('mc_tta_list/', include('_mc_tta_list.urls')),
    #path('mc_tta_list_form/', include('_mc_tta_list_form.urls')),
    path('mc_sysrun/', include('_mc_sysrun.urls')),
    path('mc_design_menu/', include('_mc_design_menu.urls')),
    path('mc_design_menu_child/', include('_mc_design_menu_child.urls')),
    path('mc_get_tta_details/', include('_mc_get_tta_details.urls')),
    path('mc_get_tta_details_child/', include('_mc_get_tta_details_child.urls')),
    path('mc_tta_list_status/', include('_mc_tta_list_status.urls')),
    #path('mc_get_tta_status_history/', include('_mc_get_tta_status_history.urls')),
    path('mc_get_acc_user/', include('_mc_get_acc_user.urls')),
    path('mc_get_set_user/', include('_mc_get_set_user.urls')),
    path('mc_get_customer_profile/', include('_mc_get_customer_profile.urls')),
    path('mc_design_main_template/', include('_mc_design_main_template.urls')),
    #path('mc_get_design_main_template_table/', include('_mc_get_design_main_template_table.urls')),
    #path('mc_get_design_main_template_option/', include('_mc_get_design_main_template_option.urls')),
    path('mc_get_customer_profile_table/', include('_mc_get_customer_profile_table.urls')),
    path('mc_tta_logs/', include('_mc_tta_logs.urls')),
    path('mc_design_dynamic/', include('_mc_design_dynamic.urls')),
    path('mc_design_dynamic_single/', include('_mc_design_dynamic_single.urls')),
    #path('mc_rims_acc_type/', include('_mc_get_rims_acc_type.urls')),
    path('mc_get_z_data/', include('_mc_get_z_data.urls')),
    path('mc_get_customer_url/', include('_mc_get_customer_url.urls')),
    path('mc_get_acc_internal/', include('_mc_get_acc_internal.urls')),
    path('mc_tta_list_cal_main/', include('_mc_tta_list_cal_main.urls')),
    path('mc_sysrun_logic/', include('_mc_sysrun_logic.urls')),
]

# Define the list of endpoints you want to show in ml
ml_included_endpoints = [
    path('ml_rims_cp_set_branch/', include('_ml_rims_cp_set_branch.urls')),
    path('ml_rims_pay_term/', include('_ml_rims_pay_term.urls')),
    path('ml_rims_supcus/', include('_ml_rims_supcus.urls')),
    path('ml_design_cot/', include('_ml_design_cot.urls')),
    path('ml_rims_banner/', include('_ml_rims_banner.urls')),
    path('ml_rims_brand/', include('_ml_rims_brand.urls')),
    path('ml_rims_div_dept_sd_c/', include('_ml_rims_div_dept_sd_c.urls')),
    path('ml_rims_customer_data/', include('_ml_rims_customer_data.urls')),
    path('ml_rims_acc_code/', include('_ml_rims_acc_code.urls')),
    path('ml_rims_acc_glmaster/', include('_ml_rims_acc_glmaster.urls')),
]

# Define the list of endpoints you want to show in ts
ts_included_endpoints = [
    path('ts_tta_list/', include('_ts_tta_list.urls')),
    #path('ts_tta_list_cal/', include('_ts_tta_list_cal.urls')),
    path('ts_tta_action/', include('_ts_tta_action.urls')),
    path('ts_tta_cal/', include('_ts_tta_cal.urls')),
    path('ts_cal_api/', include('_ts_cal_api.urls')),
    path('ts_tta_cal_log/', include('_ts_tta_cal_log.urls')),
    path('ts_tta_cndnamt/', include('_ts_tta_cndnamt.urls')),
    path('ts_tta_invmain/', include('_ts_tta_invmain.urls')),
]

# Full API schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Panda Retail Income Management System API",
        default_version='v3',
        description="RIMS API (Full API)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Partial API schema view - for master code - example
schema_view_mc = get_schema_view(
    openapi.Info(
        title="Panda Retail Income Management System API",
        default_version='v3',
        description="RIMS API (Master Code)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=mc_included_endpoints
)

# Partial API schema view - for master list - example
schema_view_ml = get_schema_view(
    openapi.Info(
        title="Panda Retail Income Management System API",
        default_version='v3',
        description="RIMS API (Master List)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=ml_included_endpoints
)

# Partial API schema view - for transaction - example
schema_view_ts = get_schema_view(
    openapi.Info(
        title="Panda Retail Income Management System API",
        default_version='v3',
        description="RIMS API (Transaction List)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=ts_included_endpoints
)

# URLs accessed directly by the application
urlpatterns = [
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    # path('backend_rims/admin/', admin.site.urls),  # Keep this with 'backend_rims/' prefix
    # Include the django-rest-swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swaggerMC/', schema_view_mc.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-mc'),
    path('swaggerML/', schema_view_ml.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-ml'),
    path('swaggerTS/', schema_view_ts.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-ts'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

     path('admin/', admin.site.urls),
    path('tablelist/', views.tablelist, name='tablelist'),
    path('mc_design_template/', include('_mc_design_template.urls')),
    path('mc_design_tab/', include('_mc_design_tab.urls')),
    #path('mc_design_row/', include('_mc_design_row.urls')),
    #path('mc_design_column/', include('_mc_design_column.urls')),
    path('mc_design_component/', include('_mc_design_component.urls')),
    #path('mc_supcus/', include('_mc_supcus.urls')),
    #path('mc_form_option/', include('_mc_form_option.urls')),
    #path('mc_form_option_value/', include('_mc_form_option_value.urls')),
    path('mc_main_filter/', include('_mc_main_filter.urls')),
    path('mc_main_filter_child/', include('_mc_main_filter_child.urls')),
    path('mc_tta_list/', include('_mc_tta_list.urls')),
    #path('mc_tta_list_form/', include('_mc_tta_list_form.urls')),
    path('mc_sysrun/', include('_mc_sysrun.urls')),
    
    path('mc_design_menu/', include('_mc_design_menu.urls')),
    path('mc_design_menu_child/', include('_mc_design_menu_child.urls')),
    path('mc_get_tta_details/', include('_mc_get_tta_details.urls')),
    path('mc_get_tta_details_child/', include('_mc_get_tta_details_child.urls')),
    path('mc_tta_list_status/', include('_mc_tta_list_status.urls')),
    #path('mc_get_tta_status_history/', include('_mc_get_tta_status_history.urls')),
    path('mc_get_acc_user/', include('_mc_get_acc_user.urls')),
    path('mc_get_set_user/', include('_mc_get_set_user.urls')),
    path('mc_get_customer_profile/', include('_mc_get_customer_profile.urls')),
    path('mc_design_main_template/', include('_mc_design_main_template.urls')),
    #path('mc_get_design_main_template_table/', include('_mc_get_design_main_template_table.urls')),
    #path('mc_get_design_main_template_option/', include('_mc_get_design_main_template_option.urls')),
    path('mc_get_customer_profile_table/', include('_mc_get_customer_profile_table.urls')),
    path('mc_tta_logs/', include('_mc_tta_logs.urls')),
    path('ml_rims_cp_set_branch/', include('_ml_rims_cp_set_branch.urls')),
    path('ml_rims_pay_term/', include('_ml_rims_pay_term.urls')),
    path('ml_rims_supcus/', include('_ml_rims_supcus.urls')),
    path('mc_design_dynamic/', include('_mc_design_dynamic.urls')),
    path('mc_design_dynamic_single/', include('_mc_design_dynamic_single.urls')),
    path('ml_design_cot/', include('_ml_design_cot.urls')),
    path('ml_rims_banner/', include('_ml_rims_banner.urls')),
    path('ml_rims_brand/', include('_ml_rims_brand.urls')),
    path('ml_rims_div_dept_sd_c/', include('_ml_rims_div_dept_sd_c.urls')),
    path('ts_tta_list/', include('_ts_tta_list.urls')),
    #path('mc_rims_acc_type/', include('_mc_get_rims_acc_type.urls')),
    #path('ts_tta_list_cal/', include('_ts_tta_list_cal.urls')),
    path('mc_get_z_data/', include('_mc_get_z_data.urls')),
    path('mc_get_customer_url/', include('_mc_get_customer_url.urls')),
    path('mc_get_acc_internal/', include('_mc_get_acc_internal.urls')),
    path('ml_rims_customer_data/', include('_ml_rims_customer_data.urls')),
    
    path('ml_rims_acc_code/', include('_ml_rims_acc_code.urls')),
    path('ml_rims_acc_glmaster/', include('_ml_rims_acc_glmaster.urls')),
    
    path('mc_tta_list_cal_main/', include('_mc_tta_list_cal_main.urls')),
    path('mc_sysrun_logic/', include('_mc_sysrun_logic.urls')),

    path('ts_tta_action/', include('_ts_tta_action.urls')),
    path('ts_tta_cal/', include('_ts_tta_cal.urls')),
    path('ts_cal_api/', include('_ts_cal_api.urls')),
    
    path('ts_tta_cal_log/', include('_ts_tta_cal_log.urls')),
    path('ts_tta_cndnamt/', include('_ts_tta_cndnamt.urls')),
    path('ts_tta_invmain/', include('_ts_tta_invmain.urls')),
]
