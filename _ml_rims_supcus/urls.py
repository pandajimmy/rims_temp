from django.urls import include, path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ml_RimsSupcus', views.RimsSupcusViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]  

def paginate_queryset(self, queryset, request, view=None):
    if 'all' in request.query_params:
        return None

    return super().paginate_queryset(queryset, request, view)