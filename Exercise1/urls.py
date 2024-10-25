from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dogapi.views import DogViewSet, BreedViewSet

router = routers.SimpleRouter()
router.register(r'api/dogs', DogViewSet)
router.register(r'api/breeds', BreedViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

