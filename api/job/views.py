from rest_framework import generics
from api.permissions import IsAuthor
from models.model_job.models import Job
from models.model_job.serializers import JobSerializer, JobViewSerializer


# Create your views here.


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobViewSerializer


class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobViewSerializer


class JobCreateAPIView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobUpdateAPIView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthor]


class JobDeleteAPIView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthor]
