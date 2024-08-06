from django.db import models

# Create your models here.

class Artist (models.Model):
    name = models.CharField(max_length=60, null=False)
    place = models.CharField(max_length=40, null=False)
    picture = models.ImageField(upload_to='artist_images')
    
    def __str__(self) -> str:
        return self.name

class Album (models.Model):
    tittle = models.CharField(max_length=50, null=False)
    year_release = models.DateField(null=False)
    GENDERS_TYPES = {
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('HIP-HOP', 'Hip-Hop'),
        ('JAZZ', 'Jazz'),
        ('CLASSICAL', 'Classical'),
        ('BLUES', 'Blues'),
        ('REGGAE', 'Reggae'),
    }
    gender = models.CharField(max_length=30, choices=GENDERS_TYPES, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='album_images')
    
    def __str__(self) -> str:
        return self.tittle