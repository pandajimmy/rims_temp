from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .models import TtaListDetails

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListDetailsSerializer
from rest_framework import filters
import django_filters.rest_framework

class SingleRecordPagination(PageNumberPagination):
    page_size = 1  # Set page size to 1, i.e., one record per page
    page_size_query_param = 'page_size'
    max_page_size = 1  # Optionally enforce a maximum page size


class TtaListDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListDetails.objects.all().order_by('refno')
    serializer_class = TtaListDetailsSerializer
    pagination_class = SingleRecordPagination  # Use custom pagination class
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno','list_guid'] 
    search_fields = ['refno','list_guid']	