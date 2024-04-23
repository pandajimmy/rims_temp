from django.shortcuts import render

from .models import TtaList_ts

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaList_tsSerializer
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated
from django.db import connection
from _lib import panda
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TtaList_tsViewSet(viewsets.ModelViewSet):
    """
    to unlock permission class
    """
    #permission_classes = ([]) 
    """
    API endpoint that allows users to be viewed or edited.
    """ 
 

    queryset = TtaList_ts.objects.all().order_by('list_guid')
    
    serializer_class = TtaList_tsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'refno': ["in", "exact"], # note the 'in' field 
        'supplier_guid': ["in","exact"],
        'customer_guid': ["in","exact"],
        'list_guid' : ["in","exact"],
        'tta_period_from' : ["gte","lte"],
        'tta_period_to' : ["gte","lte"],

    }
    search_fields = ['refno','supplier_name','customer_guid','list_guid']
    page_size = 1000

 
        
    