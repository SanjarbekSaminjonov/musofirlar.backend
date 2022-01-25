from rest_framework import serializers
from .models import Media


# Serializer for other models serializers
class MediaForSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image')


# Media model serializer
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
