from django.shortcuts import render

from .models import AccInternal

# Create your views here.
from rest_framework import viewsets
from .serializers import AccInternalSerializer
from rest_framework import filters
import django_filters.rest_framework


class AccInternalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AccInternal.objects.all().order_by('internal_name')
    serializer_class = AccInternalSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['internal_name'] 
    search_fields = ['internal_name']