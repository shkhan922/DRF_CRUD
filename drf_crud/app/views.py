
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Playlist, Track, PlaylistTrack
from .serializers import PlaylistSerializer, TrackSerializer, PlaylistTrackSerializer


class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def create(self, request, *args, **kwargs):
        # Extract the tracks data from the request
        tracks_data = request.data.pop('tracks', [])

        # Create the playlist
        playlist_serializer = self.get_serializer(data=request.data)
        playlist_serializer.is_valid(raise_exception=True)
        playlist = playlist_serializer.save()

        if tracks_data:
            # Create and associate tracks with the playlist
            for track_data in tracks_data:
                # Try to get the track by ID, if not found, create it
                track_id = track_data.get('id')
                if track_id:
                    try:
                        track = Track.objects.get(pk=track_id)
                    except Track.DoesNotExist:
                        return Response(
                            {"error": f"Track with ID {track_id} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    # If 'id' is not provided, try to get the track by name
                    track_name = track_data.get('name')
                    try:
                        track = Track.objects.get(name=track_name)
                    except Track.DoesNotExist:
                        return Response(
                            {"error": f"Track with name {track_name} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                # Creating the PlaylistTrack object
                playlist_track_data = {
                    'playlist': playlist.id,
                    'track': track.id,
                    'sequence_number': track_data['sequence_number']
                }

                playlist_track_serializer = PlaylistTrackSerializer(data=playlist_track_data)
                playlist_track_serializer.is_valid(raise_exception=True)
                playlist_track_serializer.save()

        headers = self.get_success_headers(playlist_serializer.data)
        return Response(playlist_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistTrackListView(generics.ListCreateAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer

class PlaylistTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer
