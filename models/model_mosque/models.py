from django.db import models
from model_location.models import City

# Create your models here.


class Mosque(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='mosques', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    location_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'mosque'
        verbose_name_plural = 'mosques'

    def __str__(self):
        return self.name
