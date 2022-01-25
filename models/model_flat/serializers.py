from rest_framework import serializers
from .models import Flat
from accounts.serializers import UserForSerializer
from model_location.serializers import CitySerializer
from model_media.serializers import MediaForSerializer


class FlatSerializer(serializers.ModelSerializer):
    user = UserForSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    images = MediaForSerializer(read_only=True, many=True)

    class Meta:
        model = Flat
        fields = '__all__'
