from django.urls import path
from . import views


urlpatterns = [
    path('', views.FlatListAPIView.as_view()),
    path('create/', views.FlatCreateAPIView.as_view()),
    path('<str:pk>/', views.FlatDetailUpdateDeleteAPIView.as_view()),
]
