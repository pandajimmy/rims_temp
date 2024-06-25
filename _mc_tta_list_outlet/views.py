from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import TtaListOutlet
from .serializers import TtaListOutletSerializer
from _mc_tta_list_display_incentive_table.models import TtaListDisplayIncentiveTable
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from _lib import panda
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
        instance = serializer.instance
        old_branch_guid = instance.branch_guid
        new_branch_guid = serializer.validated_data.get('branch_guid')
        
        if old_branch_guid != new_branch_guid:
            if new_branch_guid:
                instance.branch_guid = new_branch_guid
        
        instance.save()  # Save the instance with the updated fields

    @action(detail=False, methods=['post'])
    def update_outlets(self, request):
        data = request.data

        if isinstance(data, dict):
            data = [data]

        if not isinstance(data, list):
            return Response({"error": "Data should be a list of outlets"}, status=status.HTTP_400_BAD_REQUEST)

        if not data:
            list_guid = request.query_params.get('list_guid')

            if not list_guid:
                return Response({"error": "list_guid is required to delete all outlets"}, status=status.HTTP_400_BAD_REQUEST)

            existing_outlets = TtaListOutlet.objects.filter(list_guid=list_guid)

            if existing_outlets.exists():
                for outlet in existing_outlets:
                    if TtaListDisplayIncentiveTable.objects.filter(branch_guid=outlet.branch_guid, list_guid=list_guid).exists():
                        branch_code = self.get_outlet_code(outlet.branch_guid)
                        return Response({"error": f"Display incentives exist for outlet {branch_code}. Please remove incentives first."}, status=status.HTTP_400_BAD_REQUEST)

                existing_outlets.delete()
                return Response({"message": "All outlets from the selected TTA list have been deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No outlets found for the provided list_guid"}, status=status.HTTP_200_OK)

        list_guid = data[0].get('list_guid')
        if not list_guid:
            return Response({"error": "list_guid is required in the payload"}, status=status.HTTP_400_BAD_REQUEST)

        existing_outlets = TtaListOutlet.objects.filter(list_guid=list_guid)
        existing_outlet_guids = set(existing_outlets.values_list('tta_outlet_guid', flat=True))
        provided_outlet_guids = set(outlet.get('tta_outlet_guid') for outlet in data)
        existing_outlet_branch_guids = set(outlet.branch_guid for outlet in existing_outlets)
        provided_outlet_branch_guids = set(outlet.get('branch_guid') for outlet in data if outlet.get('branch_guid'))

        # Convert existing outlet branch GUIDs to a set of strings for proper comparison
        existing_outlet_branch_guids = set(str(outlet.branch_guid) for outlet in existing_outlets)

        print("Existing Outlet Branch Guids: ", existing_outlet_branch_guids)
        print("Provided Outlet Branch Guids: ", provided_outlet_branch_guids)

        # Check for display incentives associated with existing outlets that will be deleted
        to_delete_branch_guids = existing_outlet_branch_guids - provided_outlet_branch_guids

        print("To Delete Branch Guids: ", to_delete_branch_guids)

        for branch_guid in to_delete_branch_guids:
            if TtaListDisplayIncentiveTable.objects.filter(branch_guid=branch_guid, list_guid=list_guid).exists():
                branch_code = self.get_outlet_code(branch_guid)
                return Response({"error": f"Display incentives exist for outlet {branch_code}. Please remove incentives first."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete outlets not in provided data
        to_delete = existing_outlet_guids - provided_outlet_guids
        TtaListOutlet.objects.filter(tta_outlet_guid__in=to_delete).delete()

        # Update or create outlets
        for outlet_data in data:
            outlet_guid = outlet_data.get('tta_outlet_guid')
            if outlet_guid in existing_outlet_guids:
                outlet = TtaListOutlet.objects.get(tta_outlet_guid=outlet_guid)
                serializer = TtaListOutletSerializer(outlet, data=outlet_data, partial=True)
            else:
                outlet_data.update({
                    'outlet_type': 'Outlet',
                    'outlet_code': self.get_outlet_code(outlet_data['branch_guid']),
                    'outlet_label': self.get_outlet_label(outlet_data['branch_guid'])
                })
                serializer = TtaListOutletSerializer(data=outlet_data)

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
