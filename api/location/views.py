from rest_framework import generics

from model_location.models import Country, City
from .serializers import CountrySerializer, CitySerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityCreateAPIView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
