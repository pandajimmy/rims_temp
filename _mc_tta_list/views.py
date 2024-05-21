from django.shortcuts import render

from .models import TtaList

# Create your views here.
from rest_framework import viewsets
from .serializers import TtaListSerializer
from rest_framework import filters
import django_filters.rest_framework
import json
from django.db import connection

class TtaListViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    #TtaList.get()
    # def get(self, request, format=None):
    #     cursor = connection.cursor()
    #     cursor.execute("SET sort_buffer_size = 262144256000000")
    #     print('view_ttalist')
        

    queryset = TtaList.objects.all().order_by('refno').select_related(
        'purchase_n_rebates',
        'payment_n_discount',
        'stock_n_deliveries',
        'administration_fees',
        'business_growth_support',
        'promotion_support',
        'display_incentive',
        'marketing_support',
        'e_commerce_support',
        'condition_of_trade' 
      )
    serializer_class = TtaListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filterset_fields = ['refno','supplier_name']
    filterset_fields = {
        'refno': ["in", "exact"], # note the 'in' field
        'supplier_guid': ["in","exact"],
        'customer_guid': ["in","exact"],
        'list_guid' : ["in","exact"],
        'list_status' : ["in","exact"],
        'tta_period_from' : ["gte","lte"],
        'tta_period_to' : ["gte","lte"],
        # 'refno': [ "exact"], # note the 'in' field
        # 'supplier_guid': ["exact"],
        # 'customer_guid': ["exact"],
        # 'list_guid' : ["exact"],

    }
    search_fields = ['refno','supplier_name','customer_guid','list_guid','list_status']
 
 
    
   

    # def post(self, request, *args, **kwargs):
    #     serializer = TtaListSerializer(data=request.data)
    #     print('7688')
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #     except ValidationError:
    #         return Response({"errors": (serializer.errors,)},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response(request.data, status=status.HTTP_200_OK)
        

    
    # def save_data(request):
    #     if request.method == 'POST':
    #         json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
    #     try:
    #         data = json_data['data']
    #     except KeyError:
    #         HttpResponseServerError("Malformed data!")
    #         HttpResponse("Got json data")
 
  