from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.CountryListAPIView.as_view()),
    path('country/create/', views.CountryCreateAPIView.as_view()),
    path('country/<str:pk>/', views.CountryDetailUpdateDeleteAPIView.as_view()),

    path('city/', views.CityListAPIView.as_view()),
    path('city/create/', views.CityCreateAPIView.as_view()),
    path('city/<str:pk>/', views.CityDetailUpdateDeleteAPIView.as_view()),
]
