from rest_framework import serializers
from .models import Flat
from accounts.serializers import UserForSerializer
from model_location.serializers import CityViewSerializer
from model_media.serializers import MediaViewSerializer


# Flat model serializer
class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'


# Flat model serializer to view
class FlatViewSerializer(serializers.ModelSerializer):
    user = UserForSerializer(read_only=True)
    city = CityViewSerializer(read_only=True)
    images = MediaViewSerializer(read_only=True, many=True)

    class Meta:
        model = Flat
        fields = '__all__'
