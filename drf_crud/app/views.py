# myapp/views.py
from rest_framework import generics
from .models import Track, Playlist, PlaylistTrack
from .serializers import TrackSerializer, PlaylistSerializer, PlaylistTrackSerializer

class TrackListCreateView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistTrackListView(generics.ListCreateAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer

class PlaylistTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer
