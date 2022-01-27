from django.db import models

from uuid import uuid4

from models.model_flat.models import Flat
from models.model_embassy.models import Embassy
from models.model_canteen.models import Canteen
from models.model_mosque.models import Mosque
from models.model_taxi.models import Taxi


# Create your models here.


class MediaQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for media in self:
            media.image.delete()
        super(MediaQuerySet, self).delete(*args, **kwargs)


class Media(models.Model):

    objects = MediaQuerySet.as_manager()

    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    embassy_id = models.ForeignKey(Embassy, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    canteen_id = models.ForeignKey(Canteen, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    mosque_id = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    taxi_id = models.ForeignKey(Taxi, on_delete=models.CASCADE, related_name="images", null=True, blank=True)

    image = models.ImageField()

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = str(uuid4()) + '.' + self.image.name.split('.')[-1]
        super(Media, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(Media, self).delete(*args, **kwargs)

    def __str__(self):
        return self.image.name
