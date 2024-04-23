from django.shortcuts import render

from .models import FormOption

# Create your views here.
from rest_framework import viewsets
from .serializers import FormOptionSerializer
from rest_framework import filters
import django_filters.rest_framework


class FormOptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FormOption.objects.all().order_by('option_type')
    serializer_class = FormOptionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['option_type','description'] 
    search_fields = ['description']	