from django.db import models
from model_location.models import City


# Create your models here.


class Embassy(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='embassies', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    embassy_title = models.CharField(max_length=255, null=True, blank=True)
    map_url = models.CharField(max_length=1000, null=True, blank=True)
    site_url = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'embassy'
        verbose_name_plural = 'embassies'

    def __str__(self):
        return self.embassy_title
