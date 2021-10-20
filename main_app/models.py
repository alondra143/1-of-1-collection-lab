from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

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
