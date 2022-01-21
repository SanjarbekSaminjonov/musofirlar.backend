from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListAPIView.as_view()),
    path('create/', views.JobCreateAPIView.as_view()),
    path('<str:pk>/', views.JobDetailAPIView.as_view()),
    path('<str:pk>/update/', views.JobUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.JobDeleteAPIView.as_view()),
]
