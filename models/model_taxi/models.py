from django.db import models

# Create your models here.


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    app_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'taxi'
        verbose_name_plural = 'taxis'

    def __str__(self):
        return self.taxi_name
