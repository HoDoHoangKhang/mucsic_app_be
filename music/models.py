from django.db import models
from users.models import User, Artist

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField()
    file_url = models.FileField(upload_to='songs/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='songs/covers/', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Collaboration(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

class ListeningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    liked_at = models.DateTimeField(auto_now_add=True)
