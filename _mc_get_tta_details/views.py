from django.shortcuts import render

from .models import TtaList

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaList.objects.all().order_by('refno')
    serializer_class = TtaListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno','list_guid'] 
    search_fields = ['refno','list_guid']	