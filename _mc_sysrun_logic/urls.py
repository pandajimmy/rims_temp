from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('try_query/<str:datefrom>/<str:dateto>/', views.try_query, name='try_query'),
    path('<str:customer_guid>/', views.first_calculation, name='first_calculation'),
    # ex: /polls/5/results/
    #path('results/<str:customer_guid>', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('vote/<str:customer_guid>/', views.vote, name='vote'),
    #path('home/<str:customer_guid>/', views.home, name='home'),
    #path('pnl/<str:customer_guid>/<str:list_guid>/<str:date_from>/<str:date_to>/', views.pnl, name='pnl'),
    #path('calculate_pnl_category/<str:customer_guid>/<str:period_code>/', views.calculate_pnl_category, name='calculate_pnl_category'),
]