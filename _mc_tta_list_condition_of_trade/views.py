from django.shortcuts import render

from .models import TtaListConditionOfTrade

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListConditionOfTradeSerializer
from rest_framework import filters
import django_filters.rest_framework


class TtaListConditionOfTradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TtaListConditionOfTrade.objects.all().order_by('refno')
    serializer_class = TtaListConditionOfTradeSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['refno'] 
    search_fields = ['refno']