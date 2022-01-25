from rest_framework import generics

from model_location.models import Country, City
from model_location.serializers import CountryViewSerializer, CountrySerializer, CitySerializer, CityViewSerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryViewSerializer


class CountryCreateAPIView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryViewSerializer


class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityViewSerializer


class CityCreateAPIView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityViewSerializer


class CityUpdateAPIView(generics.UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDeleteAPIView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
