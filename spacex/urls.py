"""Register the routers."""
from django.urls import include, path
from rest_framework import routers
from launchpads import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'launchpads', views.LaunchpadViewSet, base_name='launchpads')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
