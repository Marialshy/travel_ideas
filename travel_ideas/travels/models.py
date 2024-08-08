from django.db import models
from django.utils import timezone

# Create your models here.


class TravelIdea(models.Model):
    short_description = models.CharField('short description', max_length=100, blank=False)
    detailed = models.CharField('detailed description', max_length=400, default='', blank=True)
    # FileFiled/ImageField - image

    def __str__(self) -> str:
        return self.short_description


RATING = {i: i for i in range(11)}


class Trip(models.Model):
    travel_idea = models.ForeignKey(TravelIdea, default='', on_delete=models.SET_DEFAULT)
    completed = models.DateField('date', default=timezone.now)
    experience = models.TextField
    rating = models.IntegerField(choices=RATING, default=None)
    # class TripImage - from 1 to 7 per trip
