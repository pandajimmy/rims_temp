from django.shortcuts import render

from .models import FormOptionValue

# Create your views here.
from rest_framework import viewsets
from .serializers import FormOptionValueSerializer
from rest_framework import filters
import django_filters.rest_framework


class FormOptionValueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FormOptionValue.objects.all().order_by('option_seq')
    serializer_class = FormOptionValueSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['option_type','label'] 
    search_fields = ['label']