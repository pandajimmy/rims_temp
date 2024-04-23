from django.shortcuts import render

from .models import TtaListForm

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListFormSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListFormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListForm.objects.all().order_by('group','seq')
    serializer_class = TtaListFormSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['group','key_description'] 
    search_fields = ['key_description']	