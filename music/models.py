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
    collaborators = models.ManyToManyField(Artist, related_name="collaborations", blank=True)  # Các nghệ sĩ hợp tác
    genre = models.ManyToManyField(Genre)
    file_url = models.FileField(upload_to='songs/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='songs/covers/', null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='playlist/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    songs = models.ManyToManyField(Song)  # Dùng trực tiếp ManyToManyField
    def __str__(self):
        return self.name

class ListeningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    liked_at = models.DateTimeField(auto_now_add=True)
