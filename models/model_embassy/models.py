from django.db import models
from model_location.models import City


# Create your models here.


class Embassy(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='embassies')
    address = models.TextField()

    embassy_title = models.CharField(max_length=255)
    map_url = models.CharField(max_length=1000)
    site_url = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'embassy'
        verbose_name_plural = 'embassies'

    def __str__(self):
        return self.embassy_title
