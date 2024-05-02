from django.shortcuts import render

from .models import DesignMenuChild

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignMenuChildSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignMenuChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignMenuChild.objects.all().order_by('description')
    serializer_class = DesignMenuChildSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['description'] 
    search_fields = ['description']	