# myapp/serializers.py
from rest_framework import serializers
from .models import Track, Playlist

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'artist_name', 'album_name', 'sequence_number']

class PlaylistSerializer(serializers.ModelSerializer):
    track = TrackSerializer(required=False)  # Make 'track' optional

    class Meta:
        model = Playlist
        fields = ['id', 'playlist_id', 'track', 'name']

    def create(self, validated_data):
        track_data = validated_data.pop('track', None)  # Handle the case where 'track' is not provided
        playlist = Playlist.objects.create(track=track_data, **validated_data)
        return playlist
