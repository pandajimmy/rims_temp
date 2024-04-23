from django.shortcuts import render

from .models import TtaListCalMain

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListCalMainSerializer
from rest_framework import filters
import django_filters.rest_framework

# from rest_framework.decorators import api_view, schema
# from rest_framework.response import Response
# from rest_framework.schemas import AutoSchema


class TtaListCalMainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListCalMain.objects.all().order_by('cal_guid')
    serializer_class = TtaListCalMainSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['cal_guid'] 
    search_fields = ['cal_guid']	

