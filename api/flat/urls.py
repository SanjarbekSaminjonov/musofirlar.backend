from django.urls import path
from . import views


urlpatterns = [
    path('', views.FlatListAPIView.as_view()),
    path('create/', views.FlatCreateAPIView.as_view()),
    path('<int:pk>/', views.FlatDetailAPIView.as_view()),
    path('<int:pk>/update/', views.FlatUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.FlatDeleteAPIView.as_view()),
]
