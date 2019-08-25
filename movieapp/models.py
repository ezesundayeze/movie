from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    year = models.DateField(auto_now=False, auto_now_add=False)
    length = models.IntegerField(null=True, blank=True)
    director_name = models.CharField(max_length=150, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "movie"

    def __str__(self):
        return self.title