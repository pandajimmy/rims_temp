from django.shortcuts import render

from .models import RimsDivDeptSdC

# Create your views here.
from rest_framework import viewsets
from .serializers import RimsDivDeptSdCSerializer
from rest_framework import filters
import django_filters.rest_framework


class RimsDivDeptSdCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RimsDivDeptSdC.objects.all().order_by('group_code')
    serializer_class = RimsDivDeptSdCSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid': ["in", "exact"], # note the 'in' field
        'group_code': ["in", "exact"], # note the 'in' field
        'group_desc': ["in","exact"],
        'dept': ["in","exact"],
        'dept_desc' : ["in","exact"],
        'subdept' : ["in","exact"],
        'subdeptdesc' : ["in","exact"],
        'category' : ["in","exact"],
        'category_desc' : ["in","exact"],
    }
    search_fields = ['customer_guid','group_code','group_desc','dept','dept_desc', 'subdept','subdeptdesc','category','category_desc']
    paginator = None