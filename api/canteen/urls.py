from django.urls import path
from . import views

urlpatterns = [
    path('', views.CanteenListAPIView.as_view()),
    path('create/', views.CanteenCreateAPIView.as_view()),
    path('<int:pk>/', views.CanteenDetailAPIView.as_view()),
    path('<int:pk>/update/', views.CanteenUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.CanteenDeleteAPIView.as_view()),
]