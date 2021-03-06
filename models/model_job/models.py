from django.db import models
from accounts.models import User
from model_location.models import City


# Create your models here.


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=255, null=True, blank=True)
    job_time = models.CharField(max_length=255, null=True, blank=True)
    working_hours = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return f'{self.job_title} - {self.address}, {self.city.name}'
