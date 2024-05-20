"""
Django settings for backend_rims project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--&_!hxl77uuez7(m23sk_%&9m-=ir&m@05@%f%*!&zwhb)^r7_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    'debug_toolbar',
    'nav_list',
    'django_filters',
    '_mc_design_template.apps.McDesignTemplateConfig',
    '_mc_design_tab.apps.McDesignTabConfig',
    '_mc_design_row.apps.McDesignRowConfig',
    '_mc_design_column.apps.McDesignColumnConfig',
    '_mc_design_component.apps.McDesignComponentConfig',
    '_mc_supcus.apps.McSupcusConfig',
    '_mc_form_option.apps.McFormOptionConfig',
    '_mc_form_option_value.apps.McFormOptionValueConfig',
    '_mc_main_filter.apps.McMainFilterConfig',
    '_mc_main_filter_child.apps.McMainFilterChildConfig',
    '_mc_tta_list.apps.McTtaListConfig',
    '_mc_tta_list_form.apps.McTtaListFormConfig',
    '_mc_tta_list_purchase_n_rebates.apps.McTtaListPurchaseNRebatesConfig',
    '_mc_tta_list_payment_n_discount.apps.McTtaListPaymentNDiscountConfig',
    '_mc_tta_list_stock_n_deliveries.apps.McTtaListStockNDeliveriesConfig',
    '_mc_tta_list_administration_fees.apps.McTtaListAdministrationFeesConfig',
    '_mc_tta_list_business_growth_support.apps.McTtaListBusinessGrowthSupportConfig',
    '_mc_tta_list_promotion_support.apps.McTtaListPromotionSupportConfig',
    '_mc_tta_list_display_incentive.apps.McTtaListDisplayIncentiveConfig',
    '_mc_tta_list_display_incentive_table.apps.McTtaListDisplayIncentiveTableConfig',
    '_mc_tta_list_marketing_support.apps.McTtaListMarketingSupportConfig',
    '_mc_tta_list_e_commerce_support.apps.McTtaListECommerceSupportConfig',
    '_mc_tta_list_condition_of_trade.apps.McTtaListConditionOfTradeConfig',
    '_mc_tta_list_trading_brand.apps.McTtaListTradingBrandConfig',
    '_mc_sysrun.apps.McSysrunConfig',
    '_mc_design_menu.apps.McDesignMenuConfig',
    '_mc_design_menu_child.apps.McDesignMenuChildConfig',
    '_mc_get_tta_details.apps.McGetTtaDetailsConfig',
    '_mc_get_tta_details_child.apps.McGetTtaDetailsChildConfig',
    '_mc_tta_list_status.apps.McTtaListStatusConfig',
    '_mc_get_tta_status_history.apps.McGetTtaStatusHistoryConfig',
    '_mc_get_acc_user.apps.McGetAccUserConfig',
    '_mc_get_set_user.apps.McGetSetUserConfig',
    '_mc_get_customer_profile.apps.McGetCustomerProfileConfig',
    #'_mc_get_customer_url.apps.McGetCustomerUrlConfig',
    '_mc_design_main_template.apps.McDesignMainTemplateConfig',
    '_mc_get_design_main_template_table.apps.McGetDesignMainTemplateTableConfig',
    '_mc_get_design_main_template_option.apps.McGetDesignMainTemplateOptionConfig',
    '_mc_get_customer_profile_table.apps.McGetCustomerProfileTableConfig',
    '_mc_tta_logs.apps.McTtaLogsConfig',
    '_ml_rims_cp_set_branch.apps.MlRimsCpSetBranchConfig',
    '_ml_rims_pay_term.apps.MlRimsPayTermConfig',
    '_ml_rims_supcus.apps.MlRimsSupcusConfig',
    '_mc_design_dynamic.apps.McDesignDynamicConfig',
    '_mc_design_dynamic_single.apps.McDesignDynamicSingleConfig',
    '_ml_design_cot.apps.MlDesignCotConfig',
    '_ml_rims_banner.apps.MlRimsBannerConfig',
    '_ml_rims_brand.apps.MlRimsBrandConfig',
    '_ml_rims_div_dept_sd_c.apps.MlRimsDivDeptSdCConfig',
    '_ts_tta_list.apps.TsTtaListConfig',
    #'_ts_tta_list_cal.apps.TsTtaListCalConfig',
    '_ts_tta_status_trans.apps.TsTtaStatusTransConfig',
    #'_ml_rims_acc_code.apps.MlRimsAccCodeConfig',
    #'_ml_rims_acc_glmaster.apps.MlRimsAccGlmasterConfig',
    #'_mc_get_rims_acc_type.apps.McGetRimsAccTypeConfig',
    '_mc_tta_list_cal_main.apps.McTtaListCalMainConfig',
    '_ts_tta_invmain.apps.TsTtaInvmainConfig',
    '_ts_tta_invchild.apps.TsTtaInvchildConfig',
    '_ts_tta_cndnamt.apps.TsTtaCndnamtConfig',
    '_ts_tta_cndnamt_child.apps.TsTtaCndnamtChildConfig',
    '_ml_rims_acc_code.apps.MlRimsAccCodeConfig',
    '_ml_rims_acc_glmaster.apps.MlRimsAccGlmasterConfig', 
    '_ts_tta_cal_log.apps.TsTtaCalLogConfig',
    '_mc_get_customer_url.apps.McGetCustomerUrlConfig',
    '_mc_get_acc_internal.apps.McGetAccInternalConfig',
    '_ml_rims_customer_data.apps.MlRimsCustomerDataConfig',
    
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,  # Always show the toolbar
}

ROOT_URLCONF = 'backend_rims.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_rims.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backend_rims',                          #<= database name
        'USER': 'root',
        'PASSWORD': 'panda_web',
        'HOST': 'localhost',                             #<=Based on your own setting
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE='Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

import os
ROOT_PATH = os.path.dirname(__file__)

STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    
    
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
   'PAGE_SIZE': 20,
   'DEFAULT_FILTER_BACKENDS': 'django_filters.rest_framework',
   'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication',],
   'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
   'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' 
   #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
   #'DEFAULT_PERMISSION_CLASSES': [ 'rest_framework.permissions.AllowAny'],
}


CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS=['*']