from rest_framework import serializers
from .models import User


# User serializer for other models serializers
class UserForSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number',)
