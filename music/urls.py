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
    #Lấy ra danh sách các bài hát của 1 nghệ sĩ
    path("artists/<int:pk>/songs/", ArtistSongsView.as_view(), name="artist-songs"),

    path('songs/', SongListCreateView.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),

    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),

    path('likes/', LikeListCreateView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),

    path('listening-history/', ListeningHistoryListCreateView.as_view(), name='listening-history-list-create'),
    path('listening-history/<int:pk>/', ListeningHistoryDetailView.as_view(), name='listening-history-detail'),
]
