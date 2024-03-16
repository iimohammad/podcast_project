from django.urls import path
from .views import *

urlpatterns = [
    path('episodes/create/', CreateEpisodeAPIView.as_view(), name='create-episode'),
    path('episodes/<int:pk>/mention/', MentionAPIView.as_view(), name='mention'),
    path('channels/<int:channel_id>/episodes/', ChannelEpisodesAPIView.as_view(), name='channel-episodes'),
    path('episodes/<int:pk>/', EpisodeDetailAPIView.as_view(), name='episode-detail'),
    path('episodes/<int:pk>/playback/', EpisodePlaybackAPIView.as_view(), name='episode-playback'),
]