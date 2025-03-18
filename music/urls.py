from django.urls import path
from .views import *

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),

    path('songs/', SongListCreateView.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),

    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),

    path('likes/', LikeListCreateView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),

    path('collaborations/', CollaborationListCreateView.as_view(), name='collaboration-list-create'),
    path('collaborations/<int:pk>/', CollaborationDetailView.as_view(), name='collaboration-detail'),

    path('playlist-songs/', PlaylistSongListCreateView.as_view(), name='playlist-song-list-create'),
    path('playlist-songs/<int:pk>/', PlaylistSongDetailView.as_view(), name='playlist-song-detail'),

    path('listening-history/', ListeningHistoryListCreateView.as_view(), name='listening-history-list-create'),
    path('listening-history/<int:pk>/', ListeningHistoryDetailView.as_view(), name='listening-history-detail'),
]
