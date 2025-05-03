from rest_framework import serializers
from .models import Fandom, FandomMember, PrivateMessage, GroupMessage
from users.models import User, Artist

class FandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fandom
        fields = ['id', 'name', 'description', 'created_by', 'is_deleted']
        read_only_fields = ['created_by', 'is_deleted']

class FandomMemberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fandom = serializers.PrimaryKeyRelatedField(queryset=Fandom.objects.all())
    
    class Meta:
        model = FandomMember
        fields = ['id', 'fandom', 'user', 'joined_at']
        read_only_fields = ['joined_at']

class PrivateMessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = PrivateMessage
        fields = ['id', 'sender', 'receiver', 'message', 'sent_at', 'read_at']
        read_only_fields = ['sender', 'sent_at', 'read_at']

class GroupMessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    fandom = serializers.PrimaryKeyRelatedField(queryset=Fandom.objects.all())
    
    class Meta:
        model = GroupMessage
        fields = ['id', 'fandom', 'sender', 'message', 'sent_at']
        read_only_fields = ['sender', 'sent_at']
