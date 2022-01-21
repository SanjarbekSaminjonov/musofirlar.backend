from rest_framework import serializers
from models.model_embassy.models import Embassy


class EmbassySerializer(serializers.ModelSerializer):
    class Meta:
        model = Embassy
        fields = '__all__'
