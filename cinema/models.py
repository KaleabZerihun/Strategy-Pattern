
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.FloatField(default=0.0)      
    popularity = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.title} ({self.release_date})"
