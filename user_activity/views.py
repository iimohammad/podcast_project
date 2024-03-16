from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Like, Playlist, PlaylistItem
from .serializers import (
    CommentSerializer,
    LikeSerializer,
    PlaylistSerializer,
    PlaylistItemSerializer,
)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

class PlaylistItemViewSet(viewsets.ModelViewSet):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer
    permission_classes = [IsAuthenticated]
