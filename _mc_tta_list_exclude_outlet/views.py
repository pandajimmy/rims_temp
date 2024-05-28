from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import TtaListExcludeOutlet

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListExcludeOutletSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListExcludeOutletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListExcludeOutlet.objects.all()
    serializer_class = TtaListExcludeOutletSerializer
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
        if not instance.tta_exclude_outlet_guid:
            instance.tta_exclude_outlet_guid = instance.generate_unique_guid()  # Generate unique tta_exclude_outlet_guid
        
        instance.save()  # Save the instance with the updated fields

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Check if branch_guid has changed
        instance = serializer.instance
        old_branch_guid = instance.branch_guid
        new_branch_guid = serializer.validated_data.get('branch_guid')
        
        if old_branch_guid != new_branch_guid:
            # If branch_guid has changed, update the code
            if new_branch_guid:
                instance.branch_guid =new_branch_guid
                instance.code = new_branch_guid.code
        
        instance.save()  # Save the instance with the updated fields