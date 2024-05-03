from django.shortcuts import render

from .models import TtaListDetails

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListDetailsSerializer
from rest_framework import filters
import django_filters.rest_framework

class TtaListDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListDetails.objects.all().order_by('refno')
    serializer_class = TtaListDetailsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno','list_guid'] 
    search_fields = ['refno','list_guid']	