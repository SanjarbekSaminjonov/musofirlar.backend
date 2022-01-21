from rest_framework import serializers
from models.model_canteen.models import Canteen
from api.media.serializers import MediaSerializer


class CanteenSerializer(serializers.ModelSerializer):
    images = MediaSerializer(read_only=True, many=True)

    class Meta:
        model = Canteen
        fields = '__all__'
