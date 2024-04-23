from django.shortcuts import render

from .models import DesignDynamic_S

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignDynamic_SSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignDynamic_SViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignDynamic_S.objects.all().order_by('dynamic_guid')
    serializer_class = DesignDynamic_SSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    #filterset_fields = ['customer_guid','dynamic_guid', 'tab_guid'] 
    filter_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'dynamic_guid': ["in","exact"],
        'tab_guid': ["in","exact"],
    }
    search_fields = ['customer_guid','dynamic_guid', 'tab_guid'] 
    paginator = None
