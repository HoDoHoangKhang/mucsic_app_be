from django.urls import path
from .views import (
    FandomViewSet, FandomMemberViewSet, 
    PrivateMessageViewSet, GroupMessageViewSet
)

urlpatterns = [
    # Fandom endpoints
    path('fandoms/', FandomViewSet.as_view({'get': 'list', 'post': 'create'}), name='fandom-list'),
    path('fandoms/<int:pk>/', FandomViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='fandom-detail'),
    path('fandoms/joined/', FandomViewSet.as_view({'get': 'joined'}), name='fandom-joined'),
    path('fandoms/<int:pk>/join-request/', FandomViewSet.as_view({'post': 'join_request'}), name='fandom-join-request'),
    path('fandoms/<int:pk>/members/', FandomViewSet.as_view({'get': 'members'}), name='fandom-members'),

    # FandomMember endpoints
    path('fandom-members/', FandomMemberViewSet.as_view({'get': 'list'}), name='fandom-member-list'),
    path('fandom-members/<int:pk>/', FandomMemberViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='fandom-member-detail'),
    path('fandom-members/<int:pk>/approve/', FandomMemberViewSet.as_view({'post': 'approve'}), name='fandom-member-approve'),

    # PrivateMessage endpoints
    path('private-messages/', PrivateMessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='private-message-list'),
    path('private-messages/<int:pk>/', PrivateMessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='private-message-detail'),
    path('private-messages/<int:pk>/mark-as-read/', PrivateMessageViewSet.as_view({'post': 'mark_as_read'}), name='private-message-mark-read'),

    # GroupMessage endpoints
    path('group-messages/', GroupMessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-message-list'),
    path('group-messages/<int:pk>/', GroupMessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='group-message-detail'),
]
