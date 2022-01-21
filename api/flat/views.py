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


class FlatDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


