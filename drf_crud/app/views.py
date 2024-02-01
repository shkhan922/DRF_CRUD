
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db import IntegrityError
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

    def create_or_update_tracks(self, playlist, tracks_data):
        for track_data in tracks_data:
            track_id = track_data['id']
            try:
                track = Track.objects.get(id=track_id)
                PlaylistTrack.objects.create(playlist=playlist, track=track, sequence_number=track_data['sequence_number'])
            except Track.DoesNotExist:
                raise IntegrityError(
                    f"Track with ID {track_data['id']} does not exist."
                )
            except IntegrityError:
                raise IntegrityError(
                    f"Duplicate combination of playlist_id and sequence_number for track {track_data['id']}."
                )

    def create(self, request, *args, **kwargs):
        tracks_data = request.data.pop('tracks', [])
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            playlist = serializer.save()

            # Create or update tracks for the playlist if 'tracks' data is present
            if tracks_data:
                self.create_or_update_tracks(playlist, tracks_data)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except IntegrityError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        tracks_data = request.data.pop('tracks', [])
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            playlist = serializer.save()

            # Clear existing tracks for the playlist
            instance.playlisttrack_set.all().delete()

            # Create or update tracks for the playlist if 'tracks' data is present
            if tracks_data:
                self.create_or_update_tracks(playlist, tracks_data)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)
        except IntegrityError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistTrackListView(generics.ListCreateAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer

class PlaylistTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer
