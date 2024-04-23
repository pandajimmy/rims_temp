from django.shortcuts import render

from .models import TtaListForm

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListFormSerializer
from rest_framework import filters
import django_filters.rest_framework

from rest_framework.response import Response
from rest_framework import status, viewsets

class TtaListFormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListForm.objects.all().order_by('seq')
    serializer_class = TtaListFormSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['group','key_description','list_guid'] 
    search_fields = ['group']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        queryset = self.filter_queryset(self.get_queryset()) 
        page = self.paginate_queryset(queryset) 
        if page is not None: 
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     file_list = self.request.data.getlist('file')
    #     for item in file_list:
    #         serializer.save(file=item)