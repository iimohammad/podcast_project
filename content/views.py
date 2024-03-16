import statistics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Episode
from .serializers import EpisodeSerializer


class CreateEpisodeAPIView(generics.CreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

class MentionAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Your mention logic here
        return Response({'message': 'Mention created successfully'}, status=status.HTTP_200_OK)

class ChannelEpisodesAPIView(generics.ListAPIView):
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        channel_id = self.kwargs['channel_id']
        return Episode.objects.filter(channel_id=channel_id)

class EpisodeDetailAPIView(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

class EpisodePlaybackAPIView(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        audio_file_url = instance.audio_file.url
        return Response({'audio_file_url': audio_file_url}, status=statistics.HTTP_200_OK)


