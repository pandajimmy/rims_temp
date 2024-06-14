from django.shortcuts import render

from .models import RimsCpSetBranchLocation

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsCpSetBranchLocationSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsCpSetBranchLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsCpSetBranchLocation.objects.all().order_by('customer_guid','code')
    serializer_class = RimsCpSetBranchLocationSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['customer_guid__customer_guid','code','description']
    # search_fields = ['customer_guid__customer_guid','code','description']

    filterset_fields = {
        'customer_guid__customer_guid': ["in", "exact"], # note the 'in' field
        'code': ["in","exact"],
        'description': ["in","exact"],

    }
    search_fields = ['customer_guid__customer_guid','code','description']
    paginator = None