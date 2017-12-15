from django.db import models

# Create your models here.
class Ratings(models.Model):
    user_id = models.IntegerField(blank=False)
    movie_id = models.IntegerField(blank=False)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, blank=False)
