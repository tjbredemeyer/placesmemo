'''from django.urls import path'''
from django.urls import include, path
from rest_framework import routers
from .views import PlaceViewSet


router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(
        '', 
        include(
            router.urls
        ),
    ),
    path(
        'places', 
        include(
            'rest_framework.urls', 
            namespace='rest_framework'
        ),
    ),
]
