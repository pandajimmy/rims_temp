from django.shortcuts import render

from .models import AccUser

# Create your views here.
from rest_framework import viewsets
from .serializers import AccUserSerializer
from rest_framework import filters
import django_filters.rest_framework


class AccUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AccUser.objects.all().order_by('acc_user_id')
    serializer_class = AccUserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ['acc_user_id','acc_user_password'] 
    search_fields = ['acc_user_id']	