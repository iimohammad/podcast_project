from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from user_panel.models import CustomUser,Profile,Channel
from .serializers import UserSerializer,RegisterSerializer,ProfileSerializer,ChannelSerializer

class RegisterUserApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Profile.objects.create(user=user)

        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class FollowChannelViewSet(viewsets.ViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        channel = self.get_object()
        request.user.following_channels.add(channel)
        return Response({'message': 'Channel followed successfully'}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        channel = self.get_object()
        request.user.following_channels.remove(channel)
        return Response({'message': 'Channel unfollowed successfully'}, status=status.HTTP_200_OK)

class FollowedChannelAPIView(generics.ListAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following_channels.all()