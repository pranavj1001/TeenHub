from django.db import models

# Create your models here.
class Ratings(models.Model):
    user_id = models.IntegerField(blank=False)
    movie_id = models.IntegerField(blank=False)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, blank=False)
    day = models.IntegerField(blank=False, default=1)
    month = models.IntegerField(blank=False, default=1)
    year = models.IntegerField(blank=False, default=2018)
    edited = models.IntegerField(blank=False, default=0)

class Links(models.Model):
    movie_id = models.IntegerField(blank=False)
    tmdb_id = models.IntegerField(blank=False)