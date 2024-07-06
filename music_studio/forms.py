from django import forms
from .import models

class MusicianForm(forms.ModelForm):
    class Meta :
        model = models.Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta :
        model = models.Album
        fields = ['Album_Name', 'Musician', 'Album_release_date', 'Ratings']
        widgets = {
            'Album_release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        