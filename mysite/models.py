from django.db import models

class MovieList(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    mlist = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    vid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    counter = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
