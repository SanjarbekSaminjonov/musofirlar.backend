from rest_framework import generics, permissions
from models.model_canteen.models import Canteen
from models.model_canteen.serializers import CanteenSerializer, CanteenViewSerializer


class CanteenListAPIView(generics.ListAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenViewSerializer


class CanteenDetailAPIView(generics.RetrieveAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenViewSerializer


class CanteenCreateAPIView(generics.CreateAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CanteenUpdateAPIView(generics.UpdateAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CanteenDeleteAPIView(generics.DestroyAPIView):
    queryset = Canteen.objects.all()
    serializer_class = CanteenSerializer
    permission_classes = (permissions.IsAuthenticated,)
