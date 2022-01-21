from rest_framework import serializers
from models.model_embassy.models import Embassy
from api.media.serializers import MediaSerializer


class EmbassySerializer(serializers.ModelSerializer):
    images = MediaSerializer(read_only=True, many=True)

    class Meta:
        model = Embassy
        fields = '__all__'
