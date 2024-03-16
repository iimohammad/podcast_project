from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from content.models import Episode
from .models import Comment, Like, Playlist, PlaylistItem
from .serializers import CommentSerializer, LikeSerializer, PlaylistSerializer, PlaylistItemSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class PlaylistCreateAPIView(generics.CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

class PlaylistDeleteAPIView(generics.DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

class PlaylistItemCreateAPIView(generics.CreateAPIView):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer
    permission_classes = [IsAuthenticated]

class PlaylistItemDeleteAPIView(generics.DestroyAPIView):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer
    permission_classes = [IsAuthenticated]
