from rest_framework import generics
from models.model_flat.models import Flat
from models.model_flat.serializers import FlatSerializer, FlatViewSerializer


# Create your views here.


class FlatListAPIView(generics.ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatViewSerializer


class FlatCreateAPIView(generics.CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetailAPIView(generics.RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatViewSerializer


class FlatUpdateAPIView(generics.UpdateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDeleteAPIView(generics.DestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
