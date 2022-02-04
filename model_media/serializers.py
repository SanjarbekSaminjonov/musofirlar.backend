from rest_framework import serializers
from .models import Media


# Media model serializer
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image', 'flat_id', 'embassy_id', 'canteen_id')


# Media model serializer to view
class MediaViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image')
