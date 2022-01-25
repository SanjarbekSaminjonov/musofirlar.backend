from rest_framework import generics
from models.model_job.models import Job
from models.model_job.serializers import JobSerializer, JobViewSerializer


# Create your views here.


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobViewSerializer


class JobCreateAPIView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobViewSerializer


class JobUpdateAPIView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDeleteAPIView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
