from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Genre, Album, Song, Playlist, Like, ListeningHistory
from .serializers import GenreSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, LikeSerializer, ListeningHistorySerializer

from rest_framework.permissions import IsAuthenticated


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# Lấy ra toàn bộ danh sách playlist của user
class UserPlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        playlists = Playlist.objects.filter(user=request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

# Lấy ra 1 playlist của user
class UserPlaylistDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk, user=request.user)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

# ❤️ Like API
class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

# Toggle Like (Like hoặc Unlike) cho Song
class SongLikeToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id):
        try:
            song = Song.objects.get(id=song_id, is_deleted=False)
            user = request.user

            # Kiểm tra xem user đã like bài hát này chưa
            like_exists = Like.objects.filter(user=user, song=song).exists()

            if like_exists:
                # Nếu đã like, thì unlike (xóa like)
                Like.objects.filter(user=user, song=song).delete()
                return Response({
                    "status": "success",
                    "message": "Unliked song successfully",
                    "liked": False
                })
            else:
                # Nếu chưa like, thì tạo like mới
                like = Like.objects.create(user=user, song=song)
                serializer = LikeSerializer(like)
                return Response({
                    "status": "success",
                    "message": "Liked song successfully",
                    "liked": True,
                    "data": serializer.data
                })

        except Song.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Song not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# Toggle Like (Like hoặc Unlike) cho Album
class AlbumLikeToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, album_id):
        try:
            album = Album.objects.get(id=album_id, is_deleted=False)
            user = request.user

            # Kiểm tra xem user đã like album này chưa
            like_exists = Like.objects.filter(user=user, album=album).exists()

            if like_exists:
                # Nếu đã like, thì unlike (xóa like)
                Like.objects.filter(user=user, album=album).delete()
                return Response({
                    "status": "success",
                    "message": "Unliked album successfully",
                    "liked": False
                })
            else:
                # Nếu chưa like, thì tạo like mới
                like = Like.objects.create(user=user, album=album)
                serializer = LikeSerializer(like)
                return Response({
                    "status": "success",
                    "message": "Liked album successfully",
                    "liked": True,
                    "data": serializer.data
                })

        except Album.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Album not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# Kiểm tra trạng thái like cho song
class CheckSongLikeStatusView(APIView):
    permission_classes = [IsAuthenticated]  # Yêu cầu user phải đăng nhập

    def get(self, request, song_id):
        user = request.user
        liked = Like.objects.filter(user=user, song_id=song_id).exists()
        return Response({"liked": liked})

# Kiểm tra trạng thái like cho album
class CheckAlbumLikeStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, album_id):
        user = request.user
        try:
            album = Album.objects.get(id=album_id, is_deleted=False)
            liked = Like.objects.filter(user=user, album=album).exists()
            return Response({"liked": liked})
        except Album.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Album not found"
            }, status=status.HTTP_404_NOT_FOUND)

# ListeningHistory API
class ListeningHistoryListCreateView(generics.ListCreateAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer

class ListeningHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer