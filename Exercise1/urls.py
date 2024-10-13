from django.contrib import admin
from django.urls import path
from dogapi.views import DogList, DogDetail, BreedList, BreedDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]
