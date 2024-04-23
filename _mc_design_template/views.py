from django.shortcuts import render

from .models import DesignTemplate

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignTemplateSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignTemplate.objects.all().order_by('description')
    serializer_class = DesignTemplateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['template_guid','description'] 
    search_fields = ['description']