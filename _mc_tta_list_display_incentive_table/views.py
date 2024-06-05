from rest_framework import viewsets
from .models import TtaListDisplayIncentiveTable, CustomerProfile
from _ml_rims_cp_set_branch.models import RimsCpSetBranch
from .serializers import TtaListDisplayIncentiveTableSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
import django_filters.rest_framework
from django.utils import timezone
import datetime

class TtaListDisplayIncentiveTableViewSet(viewsets.ModelViewSet):
    queryset = TtaListDisplayIncentiveTable.objects.all().order_by('list_guid')
    serializer_class = TtaListDisplayIncentiveTableSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['list_guid']
    search_fields = ['list_guid']

    def get_customer_name(self, customer_guid):
        try:
            customer = CustomerProfile.objects.get(customer_guid=customer_guid)
            return customer.customer_name
        except CustomerProfile.DoesNotExist:
            return 'Unknown'
        
    def get_branch_code(self, branch_guid):
        try:
            branch = RimsCpSetBranch.objects.get(branch_guid=branch_guid)
            return branch.branch_code
        except RimsCpSetBranch.DoesNotExist:
            return 'Unknown'
    
    def get_branch_name(self, branch_guid):
        try:
            branch = RimsCpSetBranch.objects.get(branch_guid=branch_guid)
            return branch.branch_name
        except RimsCpSetBranch.DoesNotExist:
            return 'Unknown'

    def create(self, request, *args, **kwargs):
        #group_details = request.data.get('group_details', {})
        #code = group_details.get('code')
        #outlet = group_details.get('outlet')
        #percent = group_details.get('percent')
        
        customer_guid = request.data.get('customer_guid')
        customer_name = self.get_customer_name(customer_guid)
        branch_guid = request.data.get('branch_guid')
        branch_code = self.get_branch_code(branch_guid)
        branch_name = self.get_branch_name(branch_guid)

        data = request.data.copy()
        data['code'] = branch_code
        data['outlet'] = branch_name
        #data['percent'] = percent
        data['created_at'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        data['created_by'] = customer_name

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        customer_guid = self.request.data.get('customer_guid')
        customer_name = self.get_customer_name(customer_guid)
        serializer.save(updated_at=timezone.now().strftime('%Y-%m-%d %H:%M:%S'), updated_by=customer_name)
