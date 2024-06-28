from django.shortcuts import render

from .models import RimsAccType

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsAccTypeSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsAccTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsAccType.objects.all().order_by('acc_type_guid')
    serializer_class = RimsAccTypeSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['acc_type_guid','acc_type_code','acc_type_description','isactive'] 
    search_fields = ['acc_type_code','acc_type_description']