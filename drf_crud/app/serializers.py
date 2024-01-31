# # # myapp/serializers.py
# # from rest_framework import serializers
# # from .models import Track, Playlist, PlaylistTrack

# # class TrackSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Track
# #         fields = ['id', 'name', 'artist_name', 'album_name']

# # class PlaylistTrackSerializer(serializers.ModelSerializer):
# #     track_id = serializers.IntegerField(source='track.id')
# #     track_name = serializers.CharField(source='track.name')

# #     class Meta:
# #         model = PlaylistTrack
# #         fields = ['track_id', 'track_name', 'sequence_number']

# # class PlaylistSerializer(serializers.ModelSerializer):
# #     tracks = PlaylistTrackSerializer(many=True, read_only=True, source='playlisttrack_set')

# #     class Meta:
# #         model = Playlist
# #         fields = ['id', 'name', 'playlist_id', 'tracks']

# #     def create(self, validated_data):
# #         tracks_data = validated_data.pop('playlisttrack_set', [])

# #         playlist = Playlist.objects.create(**validated_data)

# #         for track_data in tracks_data:
# #             track_id = track_data.get('id')
# #             sequence_number = track_data.get('sequence_number')

# #             # Assuming 'id' is the Track id in the JSON request
# #             track = Track.objects.get(id=track_id)

# #             PlaylistTrack.objects.create(playlist=playlist, track=track, sequence_number=sequence_number)

# #         return playlist

# #     def update(self, instance, validated_data):
# #         tracks_data = validated_data.pop('playlisttrack_set', [])

# #         instance.name = validated_data.get('name', instance.name)
# #         instance.playlist_id = validated_data.get('playlist_id', instance.playlist_id)
# #         instance.save()

# #         # Clear existing tracks for the playlist
# #         instance.playlisttrack_set.all().delete()

# #         for track_data in tracks_data:
# #             track_id = track_data.get('id')
# #             sequence_number = track_data.get('sequence_number')

# #             # Assuming 'id' is the Track id in the JSON request
# #             track = Track.objects.get(id=track_id)

# #             PlaylistTrack.objects.create(playlist=instance, track=track, sequence_number=sequence_number)

# #         return instance


# # myapp/serializers.py
# from rest_framework import serializers
# from .models import Track, Playlist, PlaylistTrack

# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ['id', 'name', 'artist_name', 'album_name']

# class PlaylistTrackSerializer(serializers.ModelSerializer):
#     track = TrackSerializer()

#     class Meta:
#         model = PlaylistTrack
#         fields = ['track', 'sequence_number']

# class PlaylistSerializer(serializers.ModelSerializer):
#     tracks = PlaylistTrackSerializer(many=True, read_only=True, source='playlisttrack_set')

#     class Meta:
#         model = Playlist
#         fields = ['id', 'name', 'playlist_id', 'tracks']

    
# myapp/serializers.py
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