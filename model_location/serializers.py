from rest_framework import serializers
from .models import Country, City


# Country model serializer for the City model serializer
class CountryForCity(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# City model serializer
class CitySerializer(serializers.ModelSerializer):
    country_id = CountryForCity(read_only=True)

    class Meta:
        model = City
        fields = '__all__'


# City serializer for the Country model serializer
class CityForCountry(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city_name')


# Country model serializer
class CountrySerializer(serializers.ModelSerializer):
    cities = CityForCountry(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'

