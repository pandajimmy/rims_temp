from django.shortcuts import render

from .models import RimsBanner

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsBannerSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsBannerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsBanner.objects.all().order_by('concept')
    serializer_class = RimsBannerSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filter_fields = {
        'concept': ["in", "exact"], # note the 'in' field
        'branch': ["in","exact"],
        'customer_guid': ["exact"],
        'concept_inactive' : ["in","exact"],
        'branch_inactive' : ["in","exact"],
    }
    search_fields = ['customer_guid','concept','branch','concept_inactive', 'branch_inactive']