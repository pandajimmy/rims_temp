from django.shortcuts import render

from .models import DesignCot

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignCotSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignCotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignCot.objects.all().order_by('customer_guid','cot_description')
    serializer_class = DesignCotSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid': ["in", "exact"], # note the 'in' field
        'tab_guid': ["in","exact"],
        'cot_group': ["in","exact"],
        'cot_description': ["in","exact"],
        'isactive': ["in","exact"],
        'isdeleted': ["in","exact"]
    }
    search_fields = ['tab_guid','cot_group','cot_description','customer_guid']