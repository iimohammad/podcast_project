from django.contrib import admin
from django.urls import path
from podcastPro.local_settings import *

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
]
