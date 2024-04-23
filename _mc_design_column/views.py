from django.shortcuts import render

from .models import DesignColumn

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignColumnSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignColumnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignColumn.objects.all().order_by('seq')
    serializer_class = DesignColumnSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['seq','size'] 
    search_fields = ['seq']