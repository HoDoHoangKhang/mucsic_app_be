from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Genre, Album, Song, Playlist, Like, ListeningHistory
from .serializers import GenreSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, LikeSerializer, ListeningHistorySerializer

from rest_framework.permissions import IsAuthenticated


# 🎼 Album API
# CRUD Albums
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.filter(is_deleted=False)
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist'] #Lọc theo id artist
    def get_queryset(self):
        queryset = super().get_queryset()
        artist_id = self.request.query_params.get('artist', None)
        if artist_id:
            queryset = queryset.filter(artist_id=artist_id)
        return queryset

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.filter(is_deleted=False)
    serializer_class = AlbumSerializer

    # Xóa mềm
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

# 🎵 Genre API
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# 🎶 Song API
class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.filter(is_deleted=False)
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['artist', 'album', 'is_premium']
    search_fields = ['title', 'artist__user__username', 'album__title']  # Tìm kiếm theo tên bài hát, tên nghệ sĩ và tên album
    ordering_fields = ['title', 'is_premium']  # Chỉ sử dụng các trường có sẵn trong model
    ordering = ['title']  # Mặc định sắp xếp theo tên bài hát

    def get_queryset(self):
        queryset = super().get_queryset()
        # Lọc theo genre nếu có
        genre = self.request.query_params.get('genre', None)
        if genre:
            # Sử dụng genre__id thay vì genre__name
            queryset = queryset.filter(genre__id=genre)
        return queryset

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.filter(is_deleted=False)
    serializer_class = SongSerializer

    # Xóa mềm
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

# 🎵 Playlist API
class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

# API để thêm/xóa bài hát vào playlist
class PlaylistSongAddRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, playlist_id, song_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id, user=request.user, is_deleted=False)
            song = Song.objects.get(id=song_id, is_deleted=False)
            
            # Kiểm tra xem bài hát đã có trong playlist chưa
            if song in playlist.songs.all():
                return Response({
                    "status": "error",
                    "message": "Song already exists in playlist"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            playlist.songs.add(song)
            return Response({
                "status": "success",
                "message": "Song added to playlist successfully"
            })
            
        except Playlist.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Playlist not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Song.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Song not found"
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, playlist_id, song_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id, user=request.user, is_deleted=False)
            song = Song.objects.get(id=song_id, is_deleted=False)
            
            if song not in playlist.songs.all():
                return Response({
                    "status": "error",
                    "message": "Song not found in playlist"
                }, status=status.HTTP_404_NOT_FOUND)
            
            playlist.songs.remove(song)
            return Response({
                "status": "success",
                "message": "Song removed from playlist successfully"
            })
            
        except Playlist.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Playlist not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Song.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Song not found"
            }, status=status.HTTP_404_NOT_FOUND)

# API để lấy danh sách playlist của một user
class UserPlaylistListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Playlist.objects.filter(user_id=user_id, is_deleted=False)

# API để lấy danh sách bài hát trong một playlist
class PlaylistSongsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer
    
    def get_queryset(self):
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id, is_deleted=False)
        return playlist.songs.filter(is_deleted=False)

# API để tìm kiếm playlist
class PlaylistSearchView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        return Playlist.objects.filter(is_deleted=False)

# API để lấy danh sách playlist và bài hát của user đang đăng nhập
class UserCurrentPlaylistsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(user=user, is_deleted=False)

# API để lấy danh sách album đã like
class LikedAlbumsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlbumSerializer
    
    def get_queryset(self):
        user = self.request.user
        # Lấy danh sách album_id từ bảng Like
        liked_album_ids = Like.objects.filter(user=user, album__isnull=False).values_list('album_id', flat=True)
        # Lấy danh sách album dựa trên các id đã like
        return Album.objects.filter(id__in=liked_album_ids, is_deleted=False)