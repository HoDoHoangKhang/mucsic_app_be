from django.urls import path
from .views import *

urlpatterns = [
    # ===================== GENRE ENDPOINTS ========================================================================
    # GET  /genres/         - Lấy danh sách tất cả thể loại
    # POST /genres/         - Tạo thể loại mới
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    
    # GET    /genres/<id>/  - Lấy chi tiết một thể loại
    # PUT    /genres/<id>/  - Cập nhật thể loại
    # DELETE /genres/<id>/  - Xóa thể loại
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    # ===================== ALBUM ENDPOINTS =======================================================================
    # GET  /albums/         - Lấy danh sách tất cả album
    # POST /albums/         - Tạo album mới
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    
    # GET    /albums/<id>/  - Lấy chi tiết một album
    # PUT    /albums/<id>/  - Cập nhật album
    # DELETE /albums/<id>/  - Xóa album
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    
    path('albums/liked/', LikedAlbumsView.as_view(), name='liked-albums'),
    

    # ===================== SONG ENDPOINTS =======================================================================
    # GET  /songs/          - Lấy danh sách tất cả bài hát
    # POST /songs/          - Tạo bài hát mới
    path('songs/', SongListCreateView.as_view(), name='song-list'),
    
    # GET    /songs/<id>/   - Lấy chi tiết một bài hát
    # PUT    /songs/<id>/   - Cập nhật bài hát
    # DELETE /songs/<id>/   - Xóa bài hát
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),

    # ===================== LIKE ENDPOINTS =======================================================================
    # GET  /likes/          - Lấy danh sách tất cả lượt like
    # POST /likes/          - Tạo lượt like mới
    path('likes/', LikeListCreateView.as_view(), name='like-list'),
    
    # GET    /likes/<id>/   - Lấy chi tiết một lượt like
    # DELETE /likes/<id>/   - Xóa lượt like
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
    
    # GET /likes/check/song/<id>/  - Kiểm tra trạng thái like của một bài hát
    path('likes/check/song/<int:song_id>/', CheckSongLikeStatusView.as_view(), name='check-song-like'),
    
    # GET /likes/check/album/<id>/ - Kiểm tra trạng thái like của một album
    path('likes/check/album/<int:album_id>/', CheckAlbumLikeStatusView.as_view(), name='check-album-like'),
    
    # POST /songs/<id>/like-toggle/  - Thêm/xóa like cho bài hát
    path('songs/<int:song_id>/like-toggle/', SongLikeToggleView.as_view(), name='song-like-toggle'),
    
    # POST /albums/<id>/like-toggle/ - Thêm/xóa like cho album
    path('albums/<int:album_id>/like-toggle/', AlbumLikeToggleView.as_view(), name='album-like-toggle'),

    # ===================== LISTENING HISTORY ENDPOINTS =======================================================================
    # GET  /listening-history/      - Lấy lịch sử nghe nhạc
    # POST /listening-history/      - Thêm vào lịch sử nghe nhạc
    path('listening-history/', ListeningHistoryListCreateView.as_view(), name='listening-history-list-create'),
    
    # GET    /listening-history/<id>/ - Lấy chi tiết một mục trong lịch sử
    # DELETE /listening-history/<id>/ - Xóa một mục trong lịch sử
    path('listening-history/<int:pk>/', ListeningHistoryDetailView.as_view(), name='listening-history-detail'),

 # ===================== PLAYLIST ENDPOINTS =======================================================================
    # GET  /playlists/      - Lấy danh sách tất cả playlist
    # POST /playlists/      - Tạo playlist mới
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    
    # GET    /playlists/<id>/ - Lấy chi tiết một playlist
    # PUT    /playlists/<id>/ - Cập nhật playlist
    # DELETE /playlists/<id>/ - Xóa playlist
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    
    # POST /playlists/<id>/songs/<song_id>/ - Thêm bài hát vào playlist
    # DELETE /playlists/<id>/songs/<song_id>/ - Xóa bài hát khỏi playlist
    path('playlists/<int:playlist_id>/songs/<int:song_id>/', PlaylistSongAddRemoveView.as_view(), name='playlist-song-add-remove'),
    
    # GET /users/<user_id>/playlists/ - Lấy danh sách playlist của một user
    path('users/<int:user_id>/playlists/', UserPlaylistListView.as_view(), name='user-playlist-list'),
    
    # GET /playlists/<id>/songs/ - Lấy danh sách bài hát trong một playlist
    path('playlists/<int:playlist_id>/songs/', PlaylistSongsView.as_view(), name='playlist-songs'),
    
    # GET /playlists/search/ - Tìm kiếm playlist
    path('playlists/search/', PlaylistSearchView.as_view(), name='playlist-search'),
    
    
    # GET /me/playlists/ - Lấy danh sách playlist của user đang đăng nhập
    path('me/playlists/', UserCurrentPlaylistsView.as_view(), name='user-current-playlists'),

]
