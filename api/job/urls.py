from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListAPIView.as_view()),
    path('create/', views.JobCreateAPIView.as_view()),
    path('<str:pk>/', views.JobDetailUpdateDeleteAPIView.as_view()),
]
