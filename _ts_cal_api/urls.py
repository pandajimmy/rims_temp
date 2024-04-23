from django.urls import path

from . import views

urlpatterns = [
    # path('<str:trip_guid>/', views.first_calculation, name='first_calculation'),
    #path('tta_cal_api/', views.calculation, name='calculation'), 
    path('calculation/', views.calculation, name='calculation'), 
    path('check_cal/', views.check_cal, name='check_cal'), 
    
]