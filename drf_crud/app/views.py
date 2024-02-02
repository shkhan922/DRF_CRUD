
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.db import IntegrityError
from .models import Playlist, Track, PlaylistTrack


from .serializers import PlaylistSerializer, TrackSerializer, PlaylistTrackSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit the data.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users
        return request.user 
    # and request.user.is_staff
    

class ReadOnlyForStaffPermission(permissions.BasePermission):
    """
    Custom permission to allow read-only access for staff users.
    """
    def has_permission(self, request, view):
        # Allow GET request for all users
        if request.method == 'GET':
            return True
        
        # Deny permission for POST, PUT, and DELETE requests for staff users
        return not (request.user and request.user.is_staff)



class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [ReadOnlyForStaffPermission]

class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [ReadOnlyForStaffPermission]

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

class PlaylistTrackListView(generics.ListCreateAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer
    permission_classes = [IsAdminOrReadOnly]

class PlaylistTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer
    permission_classes = [IsAdminOrReadOnly]
