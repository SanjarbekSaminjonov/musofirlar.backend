from django.db import models
from accounts.models import User
from model_location.models import City


# Create your models here.


class Canteen(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canteens', null=True, blank=True)

    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='canteens', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    canteen_name = models.CharField(max_length=255, null=True, blank=True)
    rate = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'canteen'
        verbose_name_plural = 'canteens'

    def __str__(self):
        return self.canteen_name
