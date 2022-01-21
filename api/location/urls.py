from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.CountryListAPIView.as_view()),
    path('country/create/', views.CountryCreateAPIView.as_view()),
    path('country/<int:pk>/', views.CountryDetailAPIView.as_view()),
    path('country/<int:pk>/update/', views.CountryUpdateAPIView.as_view()),
    path('country/<int:pk>/delete/', views.CountryDeleteAPIView.as_view()),

    path('city/', views.CityListAPIView.as_view()),
    path('city/create/', views.CityCreateAPIView.as_view()),
    path('city/<int:pk>/', views.CityDetailAPIView.as_view()),
    path('city/<int:pk>/update/', views.CityUpdateAPIView.as_view()),
    path('city/<int:pk>/delete/', views.CityDeleteAPIView.as_view()),
]
