from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, Album, Song, Playlist, Like, Collaboration, PlaylistSong, ListeningHistory
from .serializers import GenreSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, LikeSerializer, CollaborationSerializer, PlaylistSongSerializer, ListeningHistorySerializer

# 🎵 Genre API
class GenreListCreateView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetailView(APIView):
    def get(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 🎼 Album API
class AlbumListCreateView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetailView(APIView):
    def get(self, request, pk):
        album = Album.objects.get(pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def put(self, request, pk):
        album = Album.objects.get(pk=pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        album = Album.objects.get(pk=pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 🎶 Song API
class SongListCreateView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetailView(APIView):
    def get(self, request, pk):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 🎵 Playlist API
class PlaylistListCreateView(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistDetailView(APIView):
    def get(self, request, pk):
        playlist = Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    def put(self, request, pk):
        playlist = Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        playlist = Playlist.objects.get(pk=pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ❤️ Like API
class LikeListCreateView(APIView):
    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeDetailView(APIView):
    def delete(self, request, pk):
        like = Like.objects.get(pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Collaboration API
class CollaborationListCreateView(APIView):
    def get(self, request):
        collaborations = Collaboration.objects.all()
        serializer = CollaborationSerializer(collaborations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollaborationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollaborationDetailView(APIView):
    def get(self, request, pk):
        try:
            collaboration = Collaboration.objects.get(pk=pk)
            serializer = CollaborationSerializer(collaboration)
            return Response(serializer.data)
        except Collaboration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            collaboration = Collaboration.objects.get(pk=pk)
            serializer = CollaborationSerializer(collaboration, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Collaboration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            collaboration = Collaboration.objects.get(pk=pk)
            collaboration.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Collaboration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# PlaylistSong API
class PlaylistSongListCreateView(APIView):
    def get(self, request):
        playlist_songs = PlaylistSong.objects.all()
        serializer = PlaylistSongSerializer(playlist_songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaylistSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistSongDetailView(APIView):
    def get(self, request, pk):
        try:
            playlist_song = PlaylistSong.objects.get(pk=pk)
            serializer = PlaylistSongSerializer(playlist_song)
            return Response(serializer.data)
        except PlaylistSong.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            playlist_song = PlaylistSong.objects.get(pk=pk)
            serializer = PlaylistSongSerializer(playlist_song, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PlaylistSong.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            playlist_song = PlaylistSong.objects.get(pk=pk)
            playlist_song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PlaylistSong.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# ListeningHistory API
class ListeningHistoryListCreateView(APIView):
    def get(self, request):
        histories = ListeningHistory.objects.all()
        serializer = ListeningHistorySerializer(histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListeningHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListeningHistoryDetailView(APIView):
    def get(self, request, pk):
        try:
            history = ListeningHistory.objects.get(pk=pk)
            serializer = ListeningHistorySerializer(history)
            return Response(serializer.data)
        except ListeningHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            history = ListeningHistory.objects.get(pk=pk)
            history.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ListeningHistory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)