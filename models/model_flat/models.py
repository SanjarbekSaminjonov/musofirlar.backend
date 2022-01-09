from django.db import models
from accounts.models import User
from model_location.models import City


# Create your models here.


class Flat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flats')

    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flats')
    address = models.TextField()

    description = models.TextField()
    phone_number = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    floor_of_flat = models.CharField(max_length=255)
    number_of_rooms = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'flat'
        verbose_name_plural = 'flats'

    def __str__(self):
        return f'{self.user_id.first_name} - {self.address}, {self.city_id.city_name}'
