from django.contrib import admin

# Register your models here.
from .models import Genre, Album, Song, Collaboration, Playlist, PlaylistSong, ListeningHistory, Like

admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Collaboration)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(ListeningHistory)
admin.site.register(Like)