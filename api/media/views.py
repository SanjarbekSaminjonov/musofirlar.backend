from rest_framework import generics
from model_media.models import Media
from .serializers import MediaSerializer


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET'])
# def all_images(request):
#     print()
#     all_img = Media.objects.all()
#     print(all_img)
#     serializers = MediaSerializer(all_img, many=True)
#     print(serializers)
#     return Response(serializers.data)


class MediaListAPIView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaCreateAPIView(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDetailAPIView(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaUpdateAPIView(generics.UpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaDeleteAPIView(generics.DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
