# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrackListCreateView, TrackDetailView,
    PlaylistViewSet, PlaylistDetailView,
    PlaylistTrackListView, PlaylistTrackDetailView,
)

router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    path('tracks/<int:pk>/', TrackDetailView.as_view(), name='track-detail'),
    path('playlisttracks/', PlaylistTrackListView.as_view(), name='playlisttrack-list'),
    path('playlisttracks/<int:pk>/', PlaylistTrackDetailView.as_view(), name='playlisttrack-detail'),
    path('', include(router.urls)),
]

