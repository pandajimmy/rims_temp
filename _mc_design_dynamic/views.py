from django.shortcuts import render

from .models import DesignDynamic

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignDynamicSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignDynamicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignDynamic.objects.all().order_by('dynamic_guid')
    serializer_class = DesignDynamicSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['customer_guid','dynamic_guid', 'tab_guid'] 
    search_fields = ['customer_guid','dynamic_guid', 'tab_guid'] 