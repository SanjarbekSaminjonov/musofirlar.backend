from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview),
    path('', include('api.location.urls')),
]
