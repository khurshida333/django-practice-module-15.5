from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add_musician/', views.add_Musician,name='add_musician'),
    path('add_album/', views.add_Album,name='add_album'),
    path('edit_musician<int:id>/', views.edit_musician,name='edit_musician'),
    path('edit_album<int:id>/', views.edit_album,name='edit_album'),
]
