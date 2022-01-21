from django.urls import path
from . import views

urlpatterns = [
    path('', views.MediaListAPIView.as_view()),
    path('create/', views.MediaCreateAPIView.as_view()),
    path('<str:pk>/', views.MediaDetailAPIView.as_view()),
    path('<str:pk>/update/', views.MediaUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.MediaDeleteAPIView.as_view()),
]
