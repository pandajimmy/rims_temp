from django.shortcuts import render

from .models import DesignComponent

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignComponentSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignComponentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignComponent.objects.all().order_by('seq')
    serializer_class = DesignComponentSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['seq','id'] 
    search_fields = ['id']	
