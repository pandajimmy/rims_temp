from django.shortcuts import render

from .models import DesignMenu

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignMenuSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignMenu.objects.all().order_by('seq')
    serializer_class = DesignMenuSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['description','isactive'] 
    search_fields = ['description','isactive']	
