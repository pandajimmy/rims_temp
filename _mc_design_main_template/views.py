from django.shortcuts import render

from .models import DesignMainTemplate

# Create your views here.
from rest_framework import viewsets
from .serializers import DesignMainTemplateSerializer
from rest_framework import filters
import django_filters.rest_framework


class DesignMainTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DesignMainTemplate.objects.all().order_by('main_name')
    serializer_class = DesignMainTemplateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['main_name','main_description','isactive','customer_guid'] 
    search_fields = ['main_name','main_description']	