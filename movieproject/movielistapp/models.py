from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=250)
    director=models.CharField(max_length=250)
    industry=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')


    def __str__(self):
        return self.moviename
