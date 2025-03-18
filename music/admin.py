from django.contrib import admin

# Register your models here.
from .models import Genre, Album, Song, Collaboration, Playlist, PlaylistSong, ListeningHistory, Like

class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]  # Lấy tất cả các cột
    search_fields = ["name"]

class AlbumAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Album._meta.fields]
    list_filter = ["artist"]
    search_fields = ["title","artist__user__last_name"]


class SongAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Song._meta.fields]
    list_filter = ["album", "artist", "genre"]  # Lọc theo Album, Artist, Genre
    search_fields = ["title", "album__title", "artist__user__last_name","genre__name"]  # Tìm kiếm theo tiêu đề, album, artist name, genre


class CollaborationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Collaboration._meta.fields]
    list_filter = ["artist"]  #
    search_fields = ["song__title","artist__user__last_name"]

class PlaylistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Playlist._meta.fields]  # Lấy tất cả các cột
    list_filter = ["name"]  #
    search_fields = ["name","user__last_name"]

class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlaylistSong._meta.fields]  # Lấy tất cả các cột
    search_fields = ["playlist__name","song__title"]

class ListeningHistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ListeningHistory._meta.fields]  # Lấy tất cả các cột

class LikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields]  # Lấy tất cả các cột

admin.site.register(Genre,GenreAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)
admin.site.register(Collaboration,CollaborationAdmin)
admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(PlaylistSong,PlaylistSongAdmin)
admin.site.register(ListeningHistory,ListeningHistoryAdmin)
admin.site.register(Like,LikeAdmin)