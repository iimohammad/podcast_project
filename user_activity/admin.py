from django.contrib import admin
from .models import Comment, Like, Playlist, PlaylistItem


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'episode', 'content', 'created_at')
    list_filter = ('user', 'episode', 'created_at')
    search_fields = ('content',)
    date_hierarchy = 'created_at'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'episode', 'created_at')
    list_filter = ('user', 'episode', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ('user',)
    search_fields = ('name',)


@admin.register(PlaylistItem)
class PlaylistItemAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'episode', 'added_at')
    list_filter = ('playlist', 'added_at')
    date_hierarchy = 'added_at'
