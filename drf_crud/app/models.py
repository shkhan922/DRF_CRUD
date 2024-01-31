# myapp/models.py
from django.db import models
    
class Track(models.Model):
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255, null=True, blank=True)
  

    def __str__(self):
        return f"{self.name} by {self.artist_name}"

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    playlist_id = models.CharField(max_length=255)
    tracks = models.ManyToManyField(Track, through='PlaylistTrack')

    def __str__(self):
        return f"Playlist: {self.playlist_id} - {self.name}"

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    sequence_number = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['playlist', 'track'], name='unique_playlist_track'),
            models.UniqueConstraint(fields=['playlist', 'sequence_number'], name='unique_playlist_sequence')
        ]

    def __str__(self):
        return f"Playlist: {self.playlist.playlist_id} - Track: {self.track.name} - Sequence: {self.sequence_number}"
