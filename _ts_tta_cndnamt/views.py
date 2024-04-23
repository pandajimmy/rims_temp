from django.shortcuts import render

from .models import TtaCndnAmt

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaCndnAmtSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaCndnAmtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaCndnAmt.objects.all().order_by('refno')
    serializer_class = TtaCndnAmtSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'refno': ["in", "exact"], # note the 'in' field 
        'cndn_guid': ["in", "exact"], # note the 'in' field 
        'trans_type': ["in", "exact"],

    }
    search_fields = ['customer_guid','refno','cndn_guid','trans_type']
    #paginator = None