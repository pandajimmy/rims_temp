from django.shortcuts import render

from .models import CustomerProfileTable

# Create your views here.
from rest_framework import viewsets
from .serializers import CustomerProfileTableSerializer
from rest_framework import filters
import django_filters.rest_framework


class CustomerProfileTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomerProfileTable.objects.all().order_by('customer_name')
    serializer_class = CustomerProfileTableSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['customer_guid','customer_name'] 
    search_fields = ['customer_name']