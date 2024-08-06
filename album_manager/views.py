from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .forms import ArtistForm, AlbumForm
from .models import Album, Artist

def artist(request):
    artists = Artist.objects.order_by('name')
    template = loader.get_template('artist.html')
    return HttpResponse(template.render({'artists': artists}, request))

def artist_info(request, artist_id):
    artist = get_object_or_404(Artist, pk= artist_id)
    template = loader.get_template('artist_info.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artist')
    else:
        form = ArtistForm()   
    return render(request, 'artist_form.html', {'form': form})

def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artist')
    else:
        form = ArtistForm(instance=artist)       
    return render(request, 'artist_form.html', {'form': form})

def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    artist.delete()
    return redirect("album_manager:artist")



def album(request):
    albums = Album.objects.order_by('gender')
    template = loader.get_template('album.html')
    return HttpResponse(template.render({'albums': albums}, request))

def album_info(request, album_id):
    album = get_object_or_404(Album, pk= album_id)
    template = loader.get_template('album_info.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:album')
    else:
        form = AlbumForm()   
    return render(request, 'album_form.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:album')
    else:
        form = AlbumForm(instance=album)       
    return render(request, 'album_form.html', {'form': form})

def delete_album(request, id):
    album = get_object_or_404(Album, pk = id)
    album.delete()
    return redirect("album_manager:album")