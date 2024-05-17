from django.shortcuts import render

from .models import TtaListTradingBrand

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListTradingBrandSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListTradingBrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListTradingBrand.objects.all().order_by('brand_guid')
    serializer_class = TtaListTradingBrandSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['brand_guid'] 
    search_fields = ['brand_guid']