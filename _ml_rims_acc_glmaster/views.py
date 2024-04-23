from django.shortcuts import render

from .models import RimsAccGlmaster

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsAccGlmasterSerializer
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated


class RimsAccGlmasterViewSet(viewsets.ModelViewSet):
    """
    to unlock permission class
    """
    #permission_classes = ([])
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsAccGlmaster.objects.all().order_by('glmaster_guid')
    serializer_class = RimsAccGlmasterSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'glmaster_guid': ["in", "exact"],
        'customer_guid': ["in", "exact"],
        'acc_code': ["in", "exact"], # note the 'in' field 
        'isactive': ["in","exact"], 

    }
    search_fields = ['glmaster_guid','customer_guid','acc_code','isactive']