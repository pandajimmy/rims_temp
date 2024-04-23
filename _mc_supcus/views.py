from django.shortcuts import render

# Create your views here.
from .models import Supcus

# Create your views here.
from rest_framework import viewsets
from .serializers import SupcusSerializer
from rest_framework import filters
import django_filters.rest_framework

from rest_framework.response import Response

class SupcusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Supcus.objects.all().order_by('name')
    serializer_class = SupcusSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['value','label']

    filter_fields = {
        'code': ["in", "exact"], # note the 'in' field
        'name': ["exact"]
    }
    search_fields = ['code','name']
    paginator = None
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response({'fafa':serializer.data})

    #     # serializer = self.get_serializer(queryset, many=True)
    #     # return Response({'data':serializer.data})