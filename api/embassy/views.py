from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from models.model_embassy.models import Embassy
from models.model_embassy.serializers import EmbassySerializer


class EmbassyListAPIView(generics.ListAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer


class EmbassyCreateAPIView(generics.CreateAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer


class EmbassyDetailAPIView(generics.RetrieveAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer


class EmbassyUpdateAPIView(generics.UpdateAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer


class EmbassyDeleteAPIView(generics.DestroyAPIView):
    queryset = Embassy.objects.all()
    serializer_class = EmbassySerializer
