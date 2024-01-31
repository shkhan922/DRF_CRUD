# myapp/admin.py
from django.contrib import admin
from .models import Track, Playlist, PlaylistTrack

class PlaylistTrackInline(admin.TabularInline):
    model = PlaylistTrack
    extra = 1

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist_name', 'album_name', 'sequence_number']

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['playlist_id', 'name']
    inlines = [PlaylistTrackInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

    class Meta:
        unique_together = ('tracks', 'sequence_number')

    def get_tracks_display(self, obj):
        return ", ".join([f"{pt.track.name} ({pt.sequence_number})" for pt in obj.playlisttrack_set.all()])
    get_tracks_display.short_description = 'Tracks'
