from rest_framework import serializers
from .models import Embassy
from model_location.serializers import CityViewSerializer
from model_media.serializers import MediaViewSerializer


# Embassy model serializer
class EmbassySerializer(serializers.ModelSerializer):
    class Meta:
        model = Embassy
        fields = '__all__'


# Embassy model serializer to view
class EmbassyViewSerializer(serializers.ModelSerializer):
    city = CityViewSerializer(read_only=True)
    images = MediaViewSerializer(read_only=True, many=True)

    class Meta:
        model = Embassy
        fields = '__all__'
