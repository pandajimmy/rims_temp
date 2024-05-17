from django.shortcuts import render

from .models import RimsSupcus

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsSupcusSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsSupcusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsSupcus.objects.all().order_by('name_reg', 'name')
    serializer_class = RimsSupcusSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    #filterset_fields = ['customer_guid','code','name', 'accountcode', 'type', 'block'] 
    filterset_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'code': ["exact"],
        'name': ["exact"],
        'accountcode': ["in"],
        'type' : ["in","exact"],
        'block' : ["exact"],
        'gst_no' : ["exact"],
        'reg_no' : ["exact"],
        'name_reg' : ["exact"],
        'term' : ["exact"],
    }
    search_fields = ['customer_guid','code','name', 'accountcode', 'type',
            'block', 'gst_no', 'reg_no', 'name_reg', 'term'] 
    paginator = None