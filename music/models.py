from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime

class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    actor = models.CharField(max_length=250)
    actor2 = models.CharField(blank=True, null=True, max_length=250, default='')
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    genre1 = models.CharField(blank=True, null=True, max_length=100, default='')
    movie_logo = models.FileField()
    new = models.BooleanField(default=False)
    detail= models.TextField(blank=True, null=True)
    video_file = models.FileField(default='')
    date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.movie_title + ' - ' + self.actor


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
