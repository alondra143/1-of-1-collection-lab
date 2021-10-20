from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, MinValueValidator

# Create your models here.
class Fish(models.Model):
    """Model definition for Fish."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField('date received')
    age = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        """Unicode representation of Fish."""
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)
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


