from django.db import models

# Create your models here.
class feed(models.Model):
    createdBy = models.IntegerField(blank=False)
    message = models.CharField(max_length=200, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(blank=False, default=0)
