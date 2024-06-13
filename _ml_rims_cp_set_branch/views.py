from django.shortcuts import render

from .models import RimsCpSetBranch

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsCpSetBranchSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsCpSetBranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsCpSetBranch.objects.all().order_by('customer_guid','branch_code')
    serializer_class = RimsCpSetBranchSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['customer_guid','branch_code','branch_name'] 
    # search_fields = ['customer_guid','branch_code','branch_name'] 

    filterset_fields = {
        'customer_guid__customer_guid': ["in", "exact"], # note the 'in' field
        'branch_code': ["in","exact"],
        'branch_name': ["in","exact"],

    }
    search_fields = ['customer_guid__customer_guid','branch_code','branch_name']
    paginator = None