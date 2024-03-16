from django.contrib import admin
from django.urls import path,include
from podcastPro.local_settings import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('',include('home.urls')),
    path('',include('user_panel.urls')),
    
    # SimpleJWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]
