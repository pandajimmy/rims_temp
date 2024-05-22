from django.shortcuts import render

from .models import RimsBrand

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsBrandSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsBrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsBrand.objects.all().order_by('description')
    serializer_class = RimsBrandSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'mcode': ["in", "exact"], # note the 'in' field
        'code': ["in","exact"],
        'description': ["in","exact"], 
    }
    search_fields = ['customer_guid','mcode','code','description']
    # paginator = None