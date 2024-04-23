from django.shortcuts import render

from .models import TtaListStatus

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListStatusSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListStatus.objects.all().order_by('status_key')
    serializer_class = TtaListStatusSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['status_key','status_description'] 
    search_fields = ['status_description']