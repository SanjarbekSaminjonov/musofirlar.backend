from rest_framework import serializers
from models.model_canteen.models import Canteen


class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = '__all__'
