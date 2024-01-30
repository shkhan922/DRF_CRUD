# # # myapp/models.py
# # from django.db import models

# # class Track(models.Model):
# #     name = models.CharField(max_length=255)
# #     artist_name = models.CharField(max_length=255)
# #     album_name = models.CharField(max_length=255)
# #     sequence_number = models.IntegerField()

# #     def __str__(self):
# #         return f"{self.name} by {self.artist_name}"

# # class Playlist(models.Model):
# #     playlist_id = models.CharField(max_length=255)
# #     track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='playlist_tracks', null=True, blank=True)
# #     sequence_number = models.IntegerField(null=True, blank=True)
# #     name = models.CharField(max_length=255)  # Make 'name' required

# #     def __str__(self):
# #         return f"Playlist: {self.playlist_id} - {self.name}"
    

# # myapp/models.py
# from django.db import models

# class Track(models.Model):
#     name = models.CharField(max_length=255)
#     artist_name = models.CharField(max_length=255)
#     album_name = models.CharField(max_length=255)
#     sequence_number = models.IntegerField()

#     def __str__(self):
#         return f"{self.name} by {self.artist_name}"

# class Playlist(models.Model):
#     name = models.CharField(max_length=255)
#     playlist_id = models.CharField(max_length=255)
#     tracks = models.ManyToManyField(Track, related_name='playlists', through='PlaylistTrack', through_fields=('playlist', 'track'))
   

#     def __str__(self):
#         return f"Playlist: {self.playlist_id} - {self.name}"

# class PlaylistTrack(models.Model):
#     playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
#     track = models.ForeignKey(Track, on_delete=models.CASCADE)
#     sequence_number = models.IntegerField()

#     class Meta:
#         unique_together = ('playlist', 'sequence_number')


# myapp/models.py
from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    sequence_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} by {self.artist_name}"

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    playlist_id = models.CharField(max_length=255)
    tracks = models.ManyToManyField(Track, related_name='playlists', through='PlaylistTrack')
   
    def __str__(self):
        return f"Playlist: {self.playlist_id} - {self.name}"

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    sequence_number = models.IntegerField()

    class Meta:
        unique_together = ('playlist', 'track', 'sequence_number')

