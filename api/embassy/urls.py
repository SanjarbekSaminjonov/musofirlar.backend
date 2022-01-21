from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmbassyListAPIView.as_view()),
    path('create/', views.EmbassyCreateAPIView.as_view()),
    path('<str:pk>/', views.EmbassyDetailAPIView.as_view()),
    path('<str:pk>/update/', views.EmbassyUpdateAPIView.as_view()),
    path('<str:pk>/delete/', views.EmbassyDeleteAPIView.as_view()),
]
