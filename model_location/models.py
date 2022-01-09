from django.db import models


# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.country_name


class City(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    city_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return f'{self.city_name}, {self.country_id.country_name}'
