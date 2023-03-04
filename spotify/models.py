from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    song_length = models.CharField(max_length=200, blank=True, default='')
    albumid = models.IntegerField(blank=False, null=True)
    songid = models.IntegerField(primary_key=True, blank=False, null=False, default='')
    artist = models.CharField(max_length=50, blank=False, default='')