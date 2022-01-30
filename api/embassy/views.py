from rest_framework import generics, permissions
from models.model_embassy.models import Embassy
from models.model_embassy.serializers import EmbassySerializer, EmbassyViewSerializer


class EmbassyListAPIView(generics.ListAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassyViewSerializer


class EmbassyDetailAPIView(generics.RetrieveAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassyViewSerializer


class EmbassyCreateAPIView(generics.CreateAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmbassyUpdateAPIView(generics.UpdateAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmbassyDeleteAPIView(generics.DestroyAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer
    permission_classes = (permissions.IsAuthenticated,)
