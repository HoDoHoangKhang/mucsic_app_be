from rest_framework import serializers
from users.serializers import ArtistSerializer
from .models import Genre, Album, Song, Playlist, ListeningHistory, Like

from mutagen.mp3 import MP3  # Import mutagen để đọc file MP3
from mutagen.wave import WAVE  # Nếu hỗ trợ WAV

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
    duration = serializers.SerializerMethodField()  # Trường custom

    class Meta:
        model = Song
        fields = '__all__'

    def get_duration(self, obj):
        """Tính thời lượng bài hát từ file nhạc."""
        if obj.file_url:
            try:
                file_path = obj.file_url.path  # Lấy đường dẫn file
                if file_path.endswith(".mp3"):
                    audio = MP3(file_path)
                elif file_path.endswith(".wav"):
                    audio = WAVE(file_path)
                else:
                    return None  # Không hỗ trợ định dạng khác
                return int(audio.info.length)  # Trả về số giây
            except Exception as e:
                return None  # Nếu lỗi, trả về None
        return None

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
