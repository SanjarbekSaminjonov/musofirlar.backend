from django.urls import path, include
from . import views

urlpatterns = [
    path('get-me/', views.get_me),
    path('', views.overview),
    path('', include('api.location.urls')),
]
