from django.db import models
from accounts.models import User
from model_location.models import City


# Create your models here.


class Canteen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canteens', null=True, blank=True)

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='canteens', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    rate = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=0)
    rate_count = models.IntegerField(null=True, blank=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def calc_rate(self, new_rate):
        self.rate_count += 1
        self.rate = (self.rate * (self.rate_count - 1) + new_rate) / self.rate_count

    class Meta:
        verbose_name = 'canteen'
        verbose_name_plural = 'canteens'

    def __str__(self):
        return self.name
