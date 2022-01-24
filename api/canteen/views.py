from rest_framework import generics
from models.model_canteen.models import Canteen
from models.model_canteen.serializers import CanteenSerializer


class CanteenListAPIView(generics.ListAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer


class CanteenCreateAPIView(generics.CreateAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer


class CanteenDetailAPIView(generics.RetrieveAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer


class CanteenUpdateAPIView(generics.UpdateAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer


class CanteenDeleteAPIView(generics.DestroyAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer
