from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import TtaListExcludeOutlet
from rest_framework import viewsets
from .serializers import TtaListExcludeOutletSerializer
from rest_framework import filters
import django_filters.rest_framework
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from rest_framework.decorators import action

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
                instance.branch_guid = new_branch_guid
        
        instance.save()  # Save the instance with the updated fields

    @action(detail=False, methods=['post'])
    def update_exclude_outlets(self, request):
        data = request.data

        if isinstance(data, dict):
            data = [data]

        if not isinstance(data, list):
            return Response({"error": "Data should be a list of outlets"}, status=status.HTTP_400_BAD_REQUEST)

        if not data:
            list_guid = request.query_params.get('list_guid')

            if not list_guid:
                return Response({"error": "list_guid is required to delete all outlets"}, status=status.HTTP_400_BAD_REQUEST)

            existing_outlets = TtaListExcludeOutlet.objects.filter(list_guid=list_guid)

            if existing_outlets.exists():
                existing_outlets.delete()
                return Response({"message": "All outlets from the selected TTA list have been deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No outlets found for the provided list_guid"}, status=status.HTTP_200_OK)

        list_guid = data[0].get('list_guid')
        if not list_guid:
            return Response({"error": "list_guid is required in the payload"}, status=status.HTTP_400_BAD_REQUEST)

        existing_outlets = TtaListExcludeOutlet.objects.filter(list_guid=list_guid)
        existing_outlet_guids = set(existing_outlets.values_list('tta_exclude_outlet_guid', flat=True))
        provided_outlet_guids = set(outlet.get('tta_exclude_outlet_guid') for outlet in data)
        existing_outlet_branch_guids = set(outlet.branch_guid for outlet in existing_outlets)
        provided_outlet_branch_guids = set(outlet.get('branch_guid') for outlet in data if outlet.get('branch_guid'))

        # Convert existing outlet branch GUIDs to a set of strings for proper comparison
        existing_outlet_branch_guids = set(str(outlet.branch_guid) for outlet in existing_outlets)

        print("Existing Outlet Branch Guids: ", existing_outlet_branch_guids)
        print("Provided Outlet Branch Guids: ", provided_outlet_branch_guids)

        # Delete outlets not in provided data
        to_delete = existing_outlet_guids - provided_outlet_guids

        print("To Delete Exclude Outlet Guids: ", to_delete)      

        TtaListExcludeOutlet.objects.filter(tta_exclude_outlet_guid__in=to_delete).delete()

        # Update or create outlets
        for outlet_data in data:
            outlet_guid = outlet_data.get('tta_exclude_outlet_guid')
            branch_guid = outlet_data['branch_guid']
            outlet_code = self.get_outlet_code(branch_guid)
            outlet_label = self.get_outlet_label(branch_guid)
            combined_outlet = f"{outlet_code} - {outlet_label}"

            if outlet_guid in existing_outlet_guids:
                # Update existing outlet
                outlet = TtaListExcludeOutlet.objects.get(tta_exclude_outlet_guid=outlet_guid)
                outlet_data.update({
                    'outlet': combined_outlet,
                })
                serializer = TtaListExcludeOutletSerializer(outlet, data=outlet_data, partial=True)
            else:
                # Create new outlet
                outlet_data.update({
                    'outlet': combined_outlet,
                })
                serializer = TtaListExcludeOutletSerializer(data=outlet_data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Outlets updated successfully"}, status=status.HTTP_200_OK)

    def get_outlet_code(self, branch_guid):
        try:
            branch = RimsCpSetBranch.objects.get(branch_guid=branch_guid)
            return branch.branch_code
        except RimsCpSetBranch.DoesNotExist:
            return "default_code"

    def get_outlet_label(self, branch_guid):
        try:
            branch = RimsCpSetBranch.objects.get(branch_guid=branch_guid)
            return branch.branch_name
        except RimsCpSetBranch.DoesNotExist:
            return "default_label"