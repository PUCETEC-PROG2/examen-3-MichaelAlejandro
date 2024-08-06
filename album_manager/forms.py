from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'name': 'Nombre del Artista',
            'place': 'Lugar de Origen',
            'picture': 'Foto del Artista'
        }
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control'}),
            'year_release': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'tittle': 'Titulo del Álbum',
            'year_release': 'Año de Lanzamiento',
            'gender': 'Género',
            'artist': 'Artista Asociado',
            'picture': 'Portada',
        }