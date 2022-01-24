from rest_framework import serializers
from .models import Canteen
from accounts.serializers import UserForSerializer
from model_media.models import Media


# Media model serializer for the Canteen model serializer
class MediaForCanteen(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image')


# Canteen model serializer
class CanteenSerializer(serializers.ModelSerializer):
    user = UserForSerializer(read_only=True)
    images = MediaForCanteen(read_only=True, many=True)

    class Meta:
        model = Canteen
        fields = '__all__'
