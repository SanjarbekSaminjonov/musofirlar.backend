from rest_framework import serializers
from models.model_flat.models import Flat
from api.media.serializers import MediaSerializer


class FlatSerializer(serializers.ModelSerializer):
    images = MediaSerializer(read_only=True, many=True)

    class Meta:
        model = Flat
        fields = '__all__'
