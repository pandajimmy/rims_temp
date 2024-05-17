from django.shortcuts import render

from .models import TtaInvchild

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaInvchildSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaInvchildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaInvchild.objects.all().order_by('invmain_guid')
    serializer_class = TtaInvchildSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'customer_guid': ["exact"], # note the 'in' field
        'invmain_guid': ["in", "exact"], # note the 'in' field 
    }
    search_fields = ['customer_guid','invmain_guid']
    #paginator = None

    # def create(self, validated_data): 
    #     invchild, created = TtaInvchild.objects.update_or_create(
    #         invchild_guid=validated_data.get('invchild_guid', None),
    #         defaults={'invchild_guid': '123123123312'})
    #     return True