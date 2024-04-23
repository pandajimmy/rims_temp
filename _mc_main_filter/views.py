from django.shortcuts import render

from .models import MainFilter

# Create your views here.
from rest_framework import viewsets
from .serializers import MainFilterSerializer
from rest_framework import filters
import django_filters.rest_framework


class MainFilterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MainFilter.objects.all().order_by('description')
    serializer_class = MainFilterSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['code','description'] 
    search_fields = ['description']