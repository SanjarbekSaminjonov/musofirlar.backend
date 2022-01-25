from rest_framework import serializers
from .models import Job
from accounts.serializers import UserForSerializer
from model_location.serializers import CityViewSerializer
from model_media.serializers import MediaViewSerializer


# Job model serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# Job model serializer to view
class JobViewSerializer(serializers.ModelSerializer):
    user = UserForSerializer(read_only=True)
    city = CityViewSerializer(read_only=True)
    images = MediaViewSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = '__all__'
