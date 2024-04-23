from django.shortcuts import render

from .models import RimsPayTerm

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsPayTermSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsPayTermViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsPayTerm.objects.all().order_by('customer_guid','code')
    serializer_class = RimsPayTermSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['customer_guid','code','description','setactive'] 
    search_fields = ['customer_guid','code','description','setactive'] 