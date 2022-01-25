from rest_framework import serializers
from .models import Country, City


# City model serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


# Country model serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# Country model serializer for the City model serializer
class CountryForCity(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# City model serializer to view
class CityViewSerializer(serializers.ModelSerializer):
    country = CountryForCity()

    class Meta:
        model = City
        fields = '__all__'


# City serializer for the Country model serializer
class CityForCountry(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


# Country model serializer to view
class CountryViewSerializer(serializers.ModelSerializer):
    cities = CityForCountry(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'

