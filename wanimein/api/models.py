from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.BooleanField(db_index=True, default=False)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_at']


class Genre(TimestampedModel):
    name = models.CharField(db_index=True, max_length=255)

    def __str__(self):
        return self.name

class Country(TimestampedModel):
    name = models.CharField(db_index=True, max_length=255)

    def __str__(self):
        return self.name


class Year(TimestampedModel):
    name = models.CharField(db_index=True, max_length=255)

    def __str__(self):
        return self.name


class Movie_Info(TimestampedModel):
    name = models.CharField(db_index=True)
    picture = models.TextField()
    type = models.IntegerField(db_index=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Movie_Genre(TimestampedModel):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Info, on_delete=models.CASCADE)


class Movie_Country(TimestampedModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Info, on_delete=models.CASCADE)


class Movie_Year(TimestampedModel):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Info, on_delete=models.CASCADE)


class User(TimestampedModel):
    login = models.CharField(db_index=True, max_length=255)
    password = models.CharField(max_length=255)