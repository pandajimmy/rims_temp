from django.shortcuts import render

from .models import RimsCustomerData

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsCustomerDataSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsCustomerDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsCustomerData.objects.all().order_by('customer_guid','module_type','list_guid')
    serializer_class = RimsCustomerDataSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['customer_guid','branch_code','branch_name'] 
    # search_fields = ['customer_guid','branch_code','branch_name'] 

    filterset_fields = {
        'customer_guid': ["in", "exact"], # note the 'in' field
        'module_type': ["in","exact"],
        'list_guid': ["in","exact"],
        #'period_code': ["in","exact"],

    }
    search_fields = ['customer_guid','module_type','list_guid']
    #paginator = None