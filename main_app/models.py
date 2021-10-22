from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator, MinValueValidator
from django.db.models import Sum
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)
# Create your models here.
# has to be defined before Fish because it will be referenced
class Toy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Fish(models.Model):
    """Model definition for Fish."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField('date received')
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        """Unicode representation of Fish."""
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})


class Feeding(models.Model):
    date = models.DateField('Date Fed')
    pellets = models.IntegerField(
        default = 1,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    time = models.CharField(
        max_length = 1,
        choices = TIMES,
        default = TIMES[0][0],
    )

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pellets} pellets in the {self.get_time_display()} on {self.date}'

