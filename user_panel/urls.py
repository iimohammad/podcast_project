from django.urls import path
from user_panel.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'follow', FollowChannelViewSet, basename='follow-channel')
router.register(r'profile', ProfileViewSet, basename='user-profile')
router.register(r'followed-channels', FollowChannelViewSet, basename='followed-channels')
urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterUserApi.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
