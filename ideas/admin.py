from django.contrib import admin
from django.utils.html import format_html
from .models import Idea, Vote, Ocenki
# Register your models here.


class Voteinline(admin.StackedInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'show_yt_url']
    list_filter = ['status']
    inlines = [
        Voteinline
    ]

    def show_yt_url(self, obj):
        if len(obj.youtube_url) is not None:
            return format_html(f'<a href="{obj.youtube_url}" target="_blank">{obj.youtube_url}</a>')
        else:
            return ''
    
    show_yt_url.short_description = 'yt link'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']


@admin.register(Ocenki)
class OcenkiAdmin(admin.ModelAdmin):
    list_display = ['school_objects', 'grade', 'description']