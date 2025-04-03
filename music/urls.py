from django.urls import path
from .views import *

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    ######## ALBUMS #######
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    # Lấy ra danh sách bài hát của album
    path("albums/<int:pk>/songs/", AlbumSongsView.as_view(), name="album-songs"),

    path('songs/', SongListCreateView.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),

    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('my-playlists/', UserPlaylistView.as_view(), name='my-playlists'),
    path('my-playlists/<int:pk>/', UserPlaylistDetailView.as_view(), name='my-playlist-detail'),

    ####### LIKE #######
    path('likes/', LikeListCreateView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
    # Kiểm tra trạng thái like
    path('likes/check/song/<int:song_id>/', CheckSongLikeStatusView.as_view(), name='check-song-like'),
    path('likes/check/album/<int:album_id>/', CheckAlbumLikeStatusView.as_view(), name='check-album-like'),
    # API like/unlike
    path('songs/<int:song_id>/like-toggle/', SongLikeToggleView.as_view(), name='song-like-toggle'),
    path('albums/<int:album_id>/like-toggle/', AlbumLikeToggleView.as_view(), name='album-like-toggle'),

    path('listening-history/', ListeningHistoryListCreateView.as_view(), name='listening-history-list-create'),
    path('listening-history/<int:pk>/', ListeningHistoryDetailView.as_view(), name='listening-history-detail'),
]
