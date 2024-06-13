from django.shortcuts import render

from .models import RimsAccCode

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsAccCodeSerializer
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated


class RimsAccCodeViewSet(viewsets.ModelViewSet):
    """
    to unlock permission class
    """
    #permission_classes = ([])
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsAccCode.objects.all().order_by('acc_guid')
    serializer_class = RimsAccCodeSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid__customer_guid': ["in", "exact"],
        'acc_type': ["in", "exact"], # note the 'in' field 
        'tta_field': ["in","exact"],
        'acc_code': ["in","exact"], 

    }
    search_fields = ['customer_guid__customer_guid','acc_type','tta_field','acc_code']