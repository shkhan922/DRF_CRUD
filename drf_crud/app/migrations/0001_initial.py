# Generated by Django 5.0.1 on 2024-01-31 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('playlist_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('album_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.playlist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.track')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(through='app.PlaylistTrack', to='app.track'),
        ),
        migrations.AddConstraint(
            model_name='playlisttrack',
            constraint=models.UniqueConstraint(fields=('playlist', 'track'), name='unique_playlist_track'),
        ),
        migrations.AddConstraint(
            model_name='playlisttrack',
            constraint=models.UniqueConstraint(fields=('playlist', 'sequence_number'), name='unique_playlist_sequence'),
        ),
    ]