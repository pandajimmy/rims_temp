from django.urls import path

from . import views

urlpatterns = [
    # path('<str:trip_guid>/', views.first_calculation, name='first_calculation'),
    path('invchild/<str:invmain_guid>/', views.invchild_insert, name='invchild_insert'), 
    path('invchild_delete/<str:invmain_guid>/', views.invchild_delete, name='invchild_delete'), 
    path('check_tta/', views.check_tta, name='tta_cal_1'),
    #path('export_excel/', views.export_excel, name='export_excel'),
    path('export_excel/<str:customer_guid>/<str:date_from>/<str:date_to>/', views.export_excel, name='export_excel'),
    #path('export_excel_cal_main/<str:customer_guid>/<str:date_from>/<str:date_to>/', views.export_excel_cal_main, name='export_excel_cal_main'),
    
]