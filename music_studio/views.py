from django.shortcuts import render,redirect
from .import forms
from .import models


# Create your views here.

def add_Musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.MusicianForm()
        return render(request, 'add_musician.html',{'musician_form': musician_form})
    
def add_Album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form = forms.AlbumForm()
        return render(request, 'add_album.html',{'album_form': album_form})
    
def edit_musician(request,id):
    musician = models.Musician.objects.get(pk=id)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST , instance=musician)
        if musician_form.is_valid():
           musician_form.save()
           return redirect('homepage')
    else:
         musician_form = forms.MusicianForm(instance=musician)
        
    return render(request, 'add_musician.html',{'musician_form': musician_form})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST , instance=album)
        if album_form.is_valid():
           album_form.save()
           return redirect('homepage')
    else:
        album_form = forms.AlbumForm(instance=album)
    return render(request, 'add_album.html',{'album_form': album_form})
    