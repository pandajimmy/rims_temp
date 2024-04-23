from django.shortcuts import render

from .models import Sysrun

# Create your views here.
from rest_framework import viewsets
from .serializers import SysrunSerializer
from rest_framework import filters
import django_filters.rest_framework

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema


class SysrunViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sysrun.objects.all().order_by('currentno')
    serializer_class = SysrunSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['currentno','type'] 
    search_fields = ['currentno']

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})