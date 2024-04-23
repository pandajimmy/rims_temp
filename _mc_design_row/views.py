from django.shortcuts import render

from .models import DesignRow

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignRowSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignRowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignRow.objects.all().order_by('seq')
    serializer_class = DesignRowSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['seq','size'] 
    search_fields = ['seq']	
