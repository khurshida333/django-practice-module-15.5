from django.db import models

# Create your models here.

class Musician(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Instrument_Type = models.CharField(max_length=100)

    def __str__(self):
        return f'Musician - {self.First_Name} {self.Last_Name}'
        

class Album(models.Model):
    Album_Name = models.CharField(max_length=50)
    Musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    Album_release_date = models.DateField()
    RATINGS_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    ]   
    Ratings = models.IntegerField(choices=RATINGS_CHOICES)

    def __str__(self):
        return f'Album - {self.Album_Name}'
        
