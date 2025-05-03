from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Fandom, FandomMember, PrivateMessage, GroupMessage
from .serializers import FandomSerializer, FandomMemberSerializer, PrivateMessageSerializer, GroupMessageSerializer
from users.models import Artist
from django.utils import timezone
from django.db import models
from rest_framework import serializers

class FandomViewSet(viewsets.ModelViewSet):
    queryset = Fandom.objects.filter(is_deleted=False)
    serializer_class = FandomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Chỉ cho phép artist tạo fandom
        if not hasattr(self.request.user, 'artist'):
            return Response(
                {"error": "Chỉ nghệ sĩ mới được tạo fandom"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save(created_by=self.request.user.artist)

    @action(detail=False, methods=['get'])
    def joined(self, request):
        # Lấy danh sách fandom mà user đã tham gia
        fandom_ids = FandomMember.objects.filter(user=request.user).values_list('fandom_id', flat=True)
        fandoms = Fandom.objects.filter(id__in=fandom_ids, is_deleted=False)
        serializer = self.get_serializer(fandoms, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def join_request(self, request, pk=None):
        fandom = self.get_object()
        if FandomMember.objects.filter(fandom=fandom, user=request.user).exists():
            return Response(
                {"error": "Bạn đã là thành viên của fandom này"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        FandomMember.objects.create(fandom=fandom, user=request.user)
        return Response(
            {"message": "Yêu cầu tham gia fandom đã được gửi"}, 
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        fandom = self.get_object()
        members = FandomMember.objects.filter(fandom=fandom)
        serializer = FandomMemberSerializer(members, many=True)
        return Response(serializer.data)

class FandomMemberViewSet(viewsets.ModelViewSet):
    queryset = FandomMember.objects.all()
    serializer_class = FandomMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Chỉ hiển thị các thành viên của fandom mà user là admin
        if hasattr(self.request.user, 'artist'):
            return FandomMember.objects.filter(fandom__created_by=self.request.user.artist)
        return FandomMember.objects.none()

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        member = self.get_object()
        if member.fandom.created_by != request.user.artist:
            return Response(
                {"error": "Bạn không có quyền phê duyệt yêu cầu này"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        member.is_approved = True
        member.save()
        return Response({"message": "Yêu cầu tham gia đã được phê duyệt"})

class PrivateMessageViewSet(viewsets.ModelViewSet):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Chỉ hiển thị tin nhắn của user hiện tại
        return PrivateMessage.objects.filter(
            models.Q(sender=self.request.user) | 
            models.Q(receiver=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        message = self.get_object()
        if message.receiver != request.user:
            return Response(
                {"error": "Bạn không có quyền đánh dấu tin nhắn này"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        message.read_at = timezone.now()
        message.save()
        return Response({"message": "Tin nhắn đã được đánh dấu là đã đọc"})

class GroupMessageViewSet(viewsets.ModelViewSet):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Chỉ hiển thị tin nhắn của các fandom mà user là thành viên
        return GroupMessage.objects.filter(
            fandom__fandommember__user=self.request.user
        )

    def perform_create(self, serializer):
        fandom = serializer.validated_data['fandom']
        if not FandomMember.objects.filter(fandom=fandom, user=self.request.user).exists():
            raise serializers.ValidationError("Bạn không phải là thành viên của fandom này")
        serializer.save(sender=self.request.user)
