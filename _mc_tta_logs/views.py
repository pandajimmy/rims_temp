from django.shortcuts import render

from .models import TtaLogs

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaLogsSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaLogsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaLogs.objects.all().order_by('log_guid')
    serializer_class = TtaLogsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'log_ref': ["in", "exact"], # note the 'in' field
        'log_guid': ["in","exact"]
    }
    search_fields = ['log_ref','log_guid']