from django.urls import include, path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ml_RimsDivDeptSdC', views.RimsDivDeptSdCViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]  