from django.shortcuts import render

from .models import TtaListStatusTrans

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListStatusTransSerializer
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated


class TtaListStatusTransViewSet(viewsets.ModelViewSet):
    """
    to unlock permission class
    """
    #permission_classes = ([])
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListStatusTrans.objects.all().order_by('customer_guid')
    serializer_class = TtaListStatusTransSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'customer_guid': ["in", "exact"], # note the 'in' field 
        'list_guid': ["in","exact"],
        'trans_guid': ["in","exact"],
        'status_key' : ["in","exact"],

    }
    search_fields = ['customer_guid','list_guid','trans_guid','status_key']