from rest_framework import generics
from model_media.models import Media
from model_media.serializers import MediaSerializer


class MediaListAPIView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDetailAPIView(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaCreateAPIView(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaUpdateAPIView(generics.UpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDeleteAPIView(generics.DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
