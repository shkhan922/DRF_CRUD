
from rest_framework import serializers
from .models import Track, Playlist, PlaylistTrack




class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'artist_name', 'album_name']

class PlaylistTrackSerializer(serializers.ModelSerializer):
    track_id = serializers.IntegerField(source='track.id')
    track_name = serializers.CharField(source='track.name')

    class Meta:
        model = PlaylistTrack
        fields = ['track_id', 'track_name', 'sequence_number']

class PlaylistSerializer(serializers.ModelSerializer):
    tracks = PlaylistTrackSerializer(many=True, read_only=True, source='playlisttrack_set')

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'playlist_id', 'tracks']