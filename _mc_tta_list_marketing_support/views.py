from django.shortcuts import render

from .models import TtaListMarketingSupport

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListMarketingSupportSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListMarketingSupportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListMarketingSupport.objects.all().order_by('refno')
    serializer_class = TtaListMarketingSupportSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno'] 
    search_fields = ['refno']