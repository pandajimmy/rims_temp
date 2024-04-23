from django.urls import path

from . import views

urlpatterns = [
    # path('<str:trip_guid>/', views.first_calculation, name='first_calculation'),
    path('check_tta/', views.check_tta, name='tta_cal_1'),
    path('tta_vendor/', views.tta_vendor, name='tta_vendor'),
    
]