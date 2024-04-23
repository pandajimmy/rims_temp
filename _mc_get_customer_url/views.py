from django.shortcuts import render

from .models import CustomerUrl

# Create your views here.
from rest_framework import viewsets
from .serializers import CustomerUrlSerializer
from rest_framework import filters
import django_filters.rest_framework


class CustomerUrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomerUrl.objects.all().order_by('customer_guid')
    serializer_class = CustomerUrlSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['customer_guid','isactive'] 
    search_fields = ['customer_guid','isactive']