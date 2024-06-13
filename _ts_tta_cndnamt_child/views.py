from django.shortcuts import render

from .models import TtaCndnAmtC

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaCndnAmtCSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaCndnAmtCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaCndnAmtC.objects.all().order_by('cndn_guid')
    serializer_class = TtaCndnAmtCSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid__customer_guid': ["exact"], # note the 'in' field
        'child_guid': ["in", "exact"], # note the 'in' field 
        'cndn_guid': ["in", "exact"], # note the 'in' field 
    }
    search_fields = ['customer_guid__customer_guid','child_guid','cndn_guid']
    #paginator = None