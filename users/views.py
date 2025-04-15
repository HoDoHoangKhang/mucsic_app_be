from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import User, Artist, Follower
from .serializers import UserSerializer, ArtistSerializer, FollowerSerializer

from music.models import Song, Album
from music.serializers import SongSerializer, AlbumSerializer


# API User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  Đăng nhập
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_deleted:
                return Response({"error": "Tài khoản đã bị vô hiệu hóa."}, status=status.HTTP_403_FORBIDDEN)

            refresh = RefreshToken.for_user(user)
            return Response({
                "user_id": user.id,
                "username": user.username,
                "role": user.role,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            })

        return Response({"error": "Sai tài khoản hoặc mật khẩu."}, status=status.HTTP_401_UNAUTHORIZED)

# API Artist
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# API Follower
class FollowerListCreateView(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class FollowerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    
# Kiểm tra trạng thái follow
class ArtistFollowStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response({"error": "Artist not found."},
                            status=status.HTTP_404_NOT_FOUND)

        is_following = Follower.objects.filter(
            follower=request.user,
            following=artist.user
        ).exists()
        return Response({"isFollowing": is_following}, status=status.HTTP_200_OK)

# Follow/Unfollow
class ArtistFollowToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response({"error": "Artist not found."}, status=status.HTTP_404_NOT_FOUND)

        follower = request.user
        following = artist.user

        if follower == following:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follower.objects.get_or_create(follower=follower, following=following)

        if not created:
            follow.delete()
            return Response({"message": "Unfollowed", "isFollowing": False}, status=status.HTTP_200_OK)

        return Response({"message": "Followed", "isFollowing": True}, status=status.HTTP_201_CREATED)