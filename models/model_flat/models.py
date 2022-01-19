from django.db import models
from accounts.models import User
from model_location.models import City


# Create your models here.


class Flat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flats', null=True, blank=True)

    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flats', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    floor_of_flat = models.CharField(max_length=255, null=True, blank=True)
    number_of_rooms = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'flat'
        verbose_name_plural = 'flats'

    def __str__(self):
        return f'{self.user_id.first_name} - {self.address}, {self.city_id.city_name}'
