from django.urls import path
from .views import *

urlpatterns = [
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('likes/create/', LikeCreateAPIView.as_view(), name='like-create'),
    path('likes/<int:pk>/delete/', LikeDeleteAPIView.as_view(), name='like-delete'),
    path('playlists/create/', PlaylistCreateAPIView.as_view(), name='playlist-create'),
    path('playlists/<int:pk>/delete/', PlaylistDeleteAPIView.as_view(), name='playlist-delete'),
    path('playlist-items/create/', PlaylistItemCreateAPIView.as_view(), name='playlist-item-create'),
    path('playlist-items/<int:pk>/delete/', PlaylistItemDeleteAPIView.as_view(), name='playlist-item-delete'),
]
