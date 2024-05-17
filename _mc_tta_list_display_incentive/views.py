from django.shortcuts import render

from .models import TtaListDisplayIncentive

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListDisplayIncentiveSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListDisplayIncentiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListDisplayIncentive.objects.all().order_by('refno')
    serializer_class = TtaListDisplayIncentiveSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno'] 
    search_fields = ['refno']