from rest_framework import serializers
from .models import User, Artist, Follower

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Trả về tất cả các trường

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Trả về tất cả thông tin của user

    class Meta:
        model = Artist
        fields = '__all__'

class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()  # Thông tin người theo dõi
    following = UserSerializer()  # Thông tin người được theo dõi

    class Meta:
        model = Follower
        fields = '__all__'
