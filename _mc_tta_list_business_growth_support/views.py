from django.shortcuts import render

from .models import TtaListBusinessGrowthSupport

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListBusinessGrowthSupportSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListBusinessGrowthSupportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListBusinessGrowthSupport.objects.all().order_by('refno')
    serializer_class = TtaListBusinessGrowthSupportSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno'] 
    search_fields = ['refno']