from django.shortcuts import render

from .models import SetUser

# Create your views here.
from rest_framework import viewsets
from .serializers import SetUserSerializer
from rest_framework import filters
import django_filters.rest_framework


class SetUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SetUser.objects.all().order_by('user_id')
    serializer_class = SetUserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
#    filterset_fields = ['user_id','user_password'] 
    filterset_fields = {
        'customer_guid': ["in", "exact"], # note the 'in' field
        'user_id': ["in", "exact"], # note the 'in' field
        'user_password': ["exact"],
       
    }
    search_fields = ['user_id', 'customer_guid']
    paginator = None