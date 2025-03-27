from django.urls import path
from .views import *

urlpatterns = [

    # User APIs
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Artist APIs
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
        # Lấy ra danh sách các bài hát của 1 nghệ sĩ
        path("artists/<int:pk>/songs/", ArtistSongsView.as_view(), name="artist-songs"),
        # Lấy ra danh sách các album của 1 nghệ sĩ
        path("artists/<int:pk>/albums/", ArtistAlbumsView.as_view(), name="artist-albums"),

    # Follower APIs
    path('followers/', FollowerListCreateView.as_view(), name='follower-list-create'),
    path('followers/<int:pk>/', FollowerDetailView.as_view(), name='follower-detail'),
    # Thêm 2 API mới
    path('artists/<int:pk>/follow-status/', ArtistFollowStatusView.as_view(), name='artist-follow-status'),
    path('artists/<int:pk>/follow-toggle/', ArtistFollowToggleView.as_view(), name='artist-follow-toggle'),

]
