from django.db import models

# Create your models here.
class News(models.Model):
    user_id = models.IntegerField(unique=True, blank=False)
    buzzfeed = models.IntegerField(blank=False, default=1)
    daily_mail = models.IntegerField(blank=False, default=1)
    entertainment_weekly = models.IntegerField(blank=False, default=1)
    ign = models.IntegerField(blank=False, default=1)
    mashable = models.IntegerField(blank=False, default=1)
    mtv_news = models.IntegerField(blank=False, default=1)
    polygon = models.IntegerField(blank=False, default=1)
    the_lad_bible = models.IntegerField(blank=False, default=1)
    ars_technica = models.IntegerField(blank=False, default=1)
    crypto_coins_news = models.IntegerField(blank=False, default=1)
    hacker_news = models.IntegerField(blank=False, default=1)
    recode = models.IntegerField(blank=False, default=1)
    techcrunch = models.IntegerField(blank=False, default=1)
    techradar = models.IntegerField(blank=False, default=1)
    the_next_web = models.IntegerField(blank=False, default=1)
    the_verge = models.IntegerField(blank=False, default=1)
    wired = models.IntegerField(blank=False, default=1)
