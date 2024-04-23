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

urlpatterns = [
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
         
    path('backend_rims/admin/', admin.site.urls),
    path('backend_rims/mc_design_template/', include('_mc_design_template.urls')),
    path('backend_rims/mc_design_tab/', include('_mc_design_tab.urls')),
    #path('backend_rims/mc_design_row/', include('_mc_design_row.urls')),
    #path('backend_rims/mc_design_column/', include('_mc_design_column.urls')),
    path('backend_rims/mc_design_component/', include('_mc_design_component.urls')),
    #path('backend_rims/mc_supcus/', include('_mc_supcus.urls')),
    #path('backend_rims/mc_form_option/', include('_mc_form_option.urls')),
    #path('backend_rims/mc_form_option_value/', include('_mc_form_option_value.urls')),
    path('backend_rims/mc_main_filter/', include('_mc_main_filter.urls')),
    path('backend_rims/mc_main_filter_child/', include('_mc_main_filter_child.urls')),
    path('backend_rims/mc_tta_list/', include('_mc_tta_list.urls')),
    #path('backend_rims/mc_tta_list_form/', include('_mc_tta_list_form.urls')),
    path('backend_rims/mc_sysrun/', include('_mc_sysrun.urls')),
    
    path('backend_rims/mc_design_menu/', include('_mc_design_menu.urls')),
    path('backend_rims/mc_design_menu_child/', include('_mc_design_menu_child.urls')),
    path('backend_rims/mc_get_tta_details/', include('_mc_get_tta_details.urls')),
    path('backend_rims/mc_get_tta_details_child/', include('_mc_get_tta_details_child.urls')),
    path('backend_rims/mc_tta_list_status/', include('_mc_tta_list_status.urls')),
    #path('backend_rims/mc_get_tta_status_history/', include('_mc_get_tta_status_history.urls')),
    path('backend_rims/mc_get_acc_user/', include('_mc_get_acc_user.urls')),
    path('backend_rims/mc_get_set_user/', include('_mc_get_set_user.urls')),
    path('backend_rims/mc_get_customer_profile/', include('_mc_get_customer_profile.urls')),
    path('backend_rims/mc_design_main_template/', include('_mc_design_main_template.urls')),
    #path('backend_rims/mc_get_design_main_template_table/', include('_mc_get_design_main_template_table.urls')),
    #path('backend_rims/mc_get_design_main_template_option/', include('_mc_get_design_main_template_option.urls')),
    path('backend_rims/mc_get_customer_profile_table/', include('_mc_get_customer_profile_table.urls')),
    path('backend_rims/mc_tta_logs/', include('_mc_tta_logs.urls')),
    path('backend_rims/ml_rims_cp_set_branch/', include('_ml_rims_cp_set_branch.urls')),
    path('backend_rims/ml_rims_pay_term/', include('_ml_rims_pay_term.urls')),
    path('backend_rims/ml_rims_supcus/', include('_ml_rims_supcus.urls')),
    path('backend_rims/mc_design_dynamic/', include('_mc_design_dynamic.urls')),
    path('backend_rims/mc_design_dynamic_single/', include('_mc_design_dynamic_single.urls')),
    path('backend_rims/ml_design_cot/', include('_ml_design_cot.urls')),
    path('backend_rims/ml_rims_banner/', include('_ml_rims_banner.urls')),
    path('backend_rims/ml_rims_brand/', include('_ml_rims_brand.urls')),
    path('backend_rims/ml_rims_div_dept_sd_c/', include('_ml_rims_div_dept_sd_c.urls')),
    path('backend_rims/ts_tta_list/', include('_ts_tta_list.urls')),
    #path('backend_rims/mc_rims_acc_type/', include('_mc_get_rims_acc_type.urls')),
    #path('backend_rims/ts_tta_list_cal/', include('_ts_tta_list_cal.urls')),
    path('backend_rims/mc_get_z_data/', include('_mc_get_z_data.urls')),
    path('backend_rims/mc_get_customer_url/', include('_mc_get_customer_url.urls')),
    path('backend_rims/mc_get_acc_internal/', include('_mc_get_acc_internal.urls')),
    path('backend_rims/ml_rims_customer_data/', include('_ml_rims_customer_data.urls')),
    
    path('backend_rims/ml_rims_acc_code/', include('_ml_rims_acc_code.urls')),
    path('backend_rims/ml_rims_acc_glmaster/', include('_ml_rims_acc_glmaster.urls')),
    
    path('backend_rims/mc_tta_list_cal_main/', include('_mc_tta_list_cal_main.urls')),

    path('backend_rims/mc_sysrun_logic/', include('_mc_sysrun_logic.urls')),

    path('backend_rims/ts_tta_action/', include('_ts_tta_action.urls')),
    path('backend_rims/ts_tta_cal/', include('_ts_tta_cal.urls')),
    path('backend_rims/ts_cal_api/', include('_ts_cal_api.urls')),
    
    path('backend_rims/ts_tta_cal_log/', include('_ts_tta_cal_log.urls')),
    path('backend_rims/ts_tta_cndnamt/', include('_ts_tta_cndnamt.urls')),


    path('backend_rims/ts_tta_invmain/', include('_ts_tta_invmain.urls')),
]
