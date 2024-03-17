from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Like, Playlist, PlaylistItem, FollowedChannel
from .serializers import (
    CommentSerializer,
    LikeSerializer,
    PlaylistSerializer,
    PlaylistItemSerializer,
    FollowedChannelSerializer,
)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class LikeViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]


class PlaylistItemViewSet(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer
    permission_classes = [IsAuthenticated]


class FollowedChannelViewSet(mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = FollowedChannel.objects.all()
    serializer_class = FollowedChannelSerializer
    permission_classes = [IsAuthenticated]
