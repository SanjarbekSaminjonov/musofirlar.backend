from rest_framework import serializers
from models.model_job.models import Job
from model_media.serializers import MediaSerializer


class JobSerializer(serializers.ModelSerializer):
    images = MediaSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = '__all__'
