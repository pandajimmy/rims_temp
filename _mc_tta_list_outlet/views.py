from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import TtaListOutlet
from .serializers import TtaListOutletSerializer
from _mc_tta_list_display_incentive_table.models import TtaListDisplayIncentiveTable
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.decorators import action

class TtaListOutletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListOutlet.objects.all()
    serializer_class = TtaListOutletSerializer
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
        if not instance.tta_outlet_guid:
            instance.tta_outlet_guid = instance.generate_unique_guid()  # Generate unique tta_outlet_guid
        
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
                instance.branch_guid = new_branch_guid
        
        instance.save()  # Save the instance with the updated fields

    @action(detail=False, methods=['post'])
    def update_outlets(self, request):
        data = request.data
        list_guid = data.get('list_guid')
        outlets_data = data.get('outlets', [])

        if not list_guid:
            return Response({"error": "list_guid is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not outlets_data:  # Handling empty input
            # Delete all existing outlets for the given list_guid
            existing_outlets = TtaListOutlet.objects.filter(list_guid=list_guid)
            existing_outlet_branch_guids = set(outlet.branch_guid for outlet in existing_outlets)
            
            # Check for display incentives associated with existing outlets
            display_incentives_exist = TtaListDisplayIncentiveTable.objects.filter(branch_guid__in=existing_outlet_branch_guids).exists()
            if display_incentives_exist:
                return Response({"error": "Display incentives exist for outlets that will be deleted. Please remove incentives first."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Delete all outlets for the given list_guid
            TtaListOutlet.objects.filter(list_guid=list_guid).delete()
            return Response({"message": "All outlets deleted successfully"}, status=status.HTTP_200_OK)

        existing_outlets = TtaListOutlet.objects.filter(list_guid=list_guid)
        existing_outlet_guids = set(existing_outlets.values_list('tta_outlet_guid', flat=True))
        provided_outlet_guids = set(outlet.get('tta_outlet_guid') for outlet in outlets_data)

        existing_outlet_branch_guids = set(outlet.branch_guid for outlet in existing_outlets)
        provided_outlet_branch_guids = set(outlet.get('branch_guid') for outlet in outlets_data if outlet.get('branch_guid'))

        # Check for display incentives associated with existing outlets that will be deleted
        to_delete_branch_guids = existing_outlet_branch_guids - provided_outlet_branch_guids
        display_incentives_exist = TtaListDisplayIncentiveTable.objects.filter(branch_guid__in=to_delete_branch_guids).exists()
        if display_incentives_exist:
            return Response({"error": "Display incentives exist for outlets that will be deleted. Please remove incentives first."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete outlets not in provided data
        to_delete = existing_outlet_guids - provided_outlet_guids
        TtaListOutlet.objects.filter(tta_outlet_guid__in=to_delete).delete()

        # Update or create outlets
        for outlet_data in outlets_data:
            outlet_guid = outlet_data.get('tta_outlet_guid')
            if outlet_guid in existing_outlet_guids:
                # Update existing outlet
                outlet = TtaListOutlet.objects.get(tta_outlet_guid=outlet_guid)
                serializer = TtaListOutletSerializer(outlet, data=outlet_data)
            else:
                # Create new outlet
                serializer = TtaListOutletSerializer(data=outlet_data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Outlets updated successfully"}, status=status.HTTP_200_OK)