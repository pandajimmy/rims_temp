from django.shortcuts import render

from .models import TtaListCalLogs

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListCalLogsSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListCalLogsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListCalLogs.objects.all().order_by('log_guid')
    serializer_class = TtaListCalLogsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'log_guid': ["in", "exact"],# note the 'in' field
        'customer_guid': ["in", "exact"], # note the 'in' field
        'list_guid': ["in","exact"],
        'log_module': ["in","exact"], 
        'log_ref': ["in","exact"], 
    }
    search_fields = ['log_guid','customer_guid','list_guid','log_module','log_ref'] 