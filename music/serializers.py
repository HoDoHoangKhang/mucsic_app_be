from rest_framework import serializers
from users.serializers import ArtistSerializer
from .models import Genre, Album, Song, Playlist, ListeningHistory, Like
from users.models import Artist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()  # Trả về toàn bộ object Album
    artist = ArtistSerializer()  # Trả về toàn bộ object Artist
    collaborators = ArtistSerializer(many=True)  # Trả về list object Artist
    genre = GenreSerializer(many=True)  # Trả về list object Genre

    class Meta:
        model = Song
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)  # Trả về toàn bộ object Album
    class Meta:
        model = Playlist
        fields = '__all__'

class ListeningHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningHistory
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    song = SongSerializer()  # Trả về toàn bộ object Album
    class Meta:
        model = Like
        fields = '__all__'
