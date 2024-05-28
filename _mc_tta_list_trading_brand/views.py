from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import TtaListTradingBrand

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListTradingBrandSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListTradingBrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListTradingBrand.objects.all()
    serializer_class = TtaListTradingBrandSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = [] 
    search_fields = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()  # This calls the save method of your serializer
        
        # Additional logic for setting fields based on related objects
        instance = serializer.instance  # Get the newly created instance
        if not instance.list_brand_guid:
            instance.list_brand_guid = instance.generate_unique_guid()  # Generate unique list_brand_guid
        
        instance.save()  # Save the instance with the updated fields

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
