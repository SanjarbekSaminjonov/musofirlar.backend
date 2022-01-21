from rest_framework import generics
from models.model_flat.models import Flat
from .serializers import FlatSerializer


# Create your views here.


class FlatListAPIView(generics.ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatCreateAPIView(generics.CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetailAPIView(generics.RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatUpdateAPIView(generics.UpdateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDeleteAPIView(generics.DestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
