from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'playlist-items', PlaylistItemViewSet)

urlpatterns = router.urls
