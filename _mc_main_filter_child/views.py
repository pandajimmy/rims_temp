from django.shortcuts import render

from .models import MainFilterChild

# Create your views here.
from rest_framework import viewsets
from .serializers import MainFilterChildSerializer
from rest_framework import filters
import django_filters.rest_framework


class MainFilterChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MainFilterChild.objects.all().order_by('seq')
    serializer_class = MainFilterChildSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['option_type','is_active'] 
    search_fields = ['option_type']	