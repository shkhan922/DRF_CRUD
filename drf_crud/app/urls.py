# myapp/urls.py
from django.urls import path
from .views import (
    TrackListCreateView, TrackDetailView,
    PlaylistListCreateView, PlaylistDetailView,
    PlaylistTrackListView, PlaylistTrackDetailView,
)

urlpatterns = [
    path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    path('tracks/<int:pk>/', TrackDetailView.as_view(), name='track-detail'),
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlisttracks/', PlaylistTrackListView.as_view(), name='playlisttrack-list'),
    path('playlisttracks/<int:pk>/', PlaylistTrackDetailView.as_view(), name='playlisttrack-detail'),
]
