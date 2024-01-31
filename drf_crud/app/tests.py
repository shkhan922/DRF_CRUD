# myapp/tests.py
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Track, Playlist

# Update TrackAPITestCase
class TrackAPITestCase(APITestCase):
    def setUp(self):
        self.track_data = {'name': 'Track 1', 'artist_name': 'Artist 1', 'album_name': 'Album 1'}
        self.track = Track.objects.create(**self.track_data)
        self.track_url = f'/api/tracks/{self.track.id}/'

    def test_create_track(self):
        response = self.client.post('/api/tracks/', self.track_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Track.objects.count(), 2)

    def test_retrieve_track(self):
        response = self.client.get(self.track_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    def test_update_track(self):
        updated_data = {'name': 'Updated Track'}
        response = self.client.patch(self.track_url, updated_data, format='json')  # Use PATCH
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Track.objects.get(id=self.track.id).name, 'Updated Track')
        self.assertEqual(Track.objects.count(), 1)  # Check the count immediately after the update


    def test_delete_track(self):
        response = self.client.delete(self.track_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Track.objects.count(), 0)


# Update PlaylistAPITestCase
class PlaylistAPITestCase(APITestCase):
    def setUp(self):
        self.playlist_data = {'name': 'Playlist 1', 'playlist_id': 'PL1'}
        self.playlist = Playlist.objects.create(**self.playlist_data)
        self.playlist_url = f'/api/playlists/{self.playlist.id}/'

    def test_create_playlist(self):
        response = self.client.post('/api/playlists/', self.playlist_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 2)

    def test_retrieve_playlist(self):
        response = self.client.get(self.playlist_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_playlist(self):
        updated_data = {'name': 'Updated Playlist'}
        response = self.client.patch(self.playlist_url, updated_data, format='json')  # Change to PATCH
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.get(id=self.playlist.id).name, 'Updated Playlist')

    def test_delete_playlist(self):
        response = self.client.delete(self.playlist_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Playlist.objects.count(), 0)


