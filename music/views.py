from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from users.models import Artist
from .models import Genre, Album, Song, Playlist, Like, Collaboration, PlaylistSong, ListeningHistory
from .serializers import GenreSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, LikeSerializer, CollaborationSerializer, PlaylistSongSerializer, ListeningHistorySerializer


# 🎼 Album API
# CRUD Albums
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# Lấy ra danh sách bài hát của album
class AlbumSongsView(APIView):
    def get(self, request, pk):
        try:
            album = Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            return Response({"error": "Album not found"}, status=status.HTTP_404_NOT_FOUND)

        songs = Song.objects.filter(album=album)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Lấy ra danh sách các bài hát của 1 nghệ sĩ
class ArtistSongsView(APIView):
    def get(self, request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)

        songs = Song.objects.filter(artist=artist)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# 🎵 Genre API
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# 🎶 Song API
class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# 🎵 Playlist API
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# ❤️ Like API
class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

# Collaboration API
class CollaborationListCreateView(generics.ListCreateAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer


class CollaborationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer


# PlaylistSong API
class PlaylistSongListCreateView(generics.ListCreateAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer

class PlaylistSongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer


# ListeningHistory API
class ListeningHistoryListCreateView(generics.ListCreateAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer

class ListeningHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer