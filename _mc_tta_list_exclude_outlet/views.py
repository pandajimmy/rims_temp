from django.shortcuts import render

from .models import TtaListExcludeOutlet

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListExcludeOutletSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListExcludeOutletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListExcludeOutlet.objects.all().order_by('list_guid')
    serializer_class = TtaListExcludeOutletSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['list_guid'] 
    search_fields = ['list_guid']