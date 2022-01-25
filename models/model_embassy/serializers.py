from rest_framework import serializers
from .models import Embassy
from model_location.serializers import CitySerializer
from model_media.serializers import MediaForSerializer


class EmbassySerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    images = MediaForSerializer(read_only=True, many=True)

    class Meta:
        model = Embassy
        fields = '__all__'
