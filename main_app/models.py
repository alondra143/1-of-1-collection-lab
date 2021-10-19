from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Fish(models.Model):
    """Model definition for Fish."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField('date posted')
    age = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        """Unicode representation of Fish."""
        pass
