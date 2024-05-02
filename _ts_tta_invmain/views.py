from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .models import TtaInvmain

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaInvmainSerializer
from rest_framework import filters
import django_filters.rest_framework

class SingleRecordPagination(PageNumberPagination):
    page_size = 1  # Set page size to 1, i.e., one record per page
    page_size_query_param = 'page_size'
    max_page_size = 1  # Optionally enforce a maximum page size

class TtaInvmainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaInvmain.objects.all().order_by('refno')
    serializer_class = TtaInvmainSerializer
    pagination_class = SingleRecordPagination  # Use custom pagination class
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'refno': ["in", "exact"], # note the 'in' field 
        'invmain_guid': ["in", "exact"], # note the 'in' field 
        'docno': ["in", "exact"], 
    }
    search_fields = ['customer_guid','refno','invmain_guid', 'docno']
    #paginator = None