from django.shortcuts import render

from .models import DesignTab

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignTabSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignTabViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignTab.objects.all().order_by('description')
    serializer_class = DesignTabSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['sequence','description','tab_guid'] 
    search_fields = ['description']	