from datetime import datetime, timedelta, timezone

import jwt
from django.contrib.auth.hashers import check_password
from django.db import models

from wanimein import settings


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
    remark = models.CharField(default=None, null=True, db_index=True)
    picture = models.TextField()
    type = models.IntegerField(db_index=True)

    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    year = models.ForeignKey(Year, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Movie_Genre(TimestampedModel):
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    movie_info = models.ForeignKey(Movie_Info, on_delete=models.RESTRICT)


class User(TimestampedModel):
    login = models.CharField(db_index=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    ip = models.CharField(db_index=True, max_length=255)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ('login', 'password')

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        # dt = datetime.now(tz=timezone.utc) + timedelta(days=7)
        token = jwt.encode({
            'id': self.pk,
            # 'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
        # return token.decode('utf-8')

    def __str__(self):
        return self.login


class Actors(TimestampedModel):
    name = models.CharField(db_index=True)
    people = models.BooleanField(db_index=True)

    def __str__(self):
        return self.name


class Movie_Details(TimestampedModel):
    name = models.CharField(db_index=True)
    picture = models.TextField()
    language = models.CharField(db_index=True)
    all_episodes = models.IntegerField(db_index=True)
    current_episodes = models.IntegerField(db_index=True)
    director = models.CharField(db_index=True)
    last_episode = models.DateTimeField()
    synopsis = models.TextField()
    views = models.IntegerField(default=0, db_index=True)

    year = models.ForeignKey(Year, on_delete=models.RESTRICT, related_name='year', default=1)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT, related_name='country', default=1)

    def __str__(self):
        return self.name


class Comment(TimestampedModel):
    text = models.TextField()
    respondent = models.IntegerField(db_index=True, null=True)

    author = models.ForeignKey(User, related_name='author', on_delete=models.RESTRICT, null=True)
    movie_details = models.ForeignKey(Movie_Details, related_name='movie_details', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.text


class Movie_Actors(TimestampedModel):
    actor = models.ForeignKey(Actors, on_delete=models.RESTRICT)
    movie_details = models.ForeignKey(Movie_Details, on_delete=models.RESTRICT)


class Episode(TimestampedModel):
    name = models.CharField(db_index=True)
    url = models.CharField(default='http:127.0.0.1/video')

    movie_details = models.ForeignKey(Movie_Details, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Collection(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    movie_details = models.ForeignKey(Movie_Details, on_delete=models.RESTRICT)


class Types(TimestampedModel):
    name = models.CharField(db_index=True)


class Tag(TimestampedModel):
    name = models.CharField(db_index=True)

    def __str__(self):
        return self.name


class Movie_Tags(TimestampedModel):
    tags = models.ForeignKey(Tag, on_delete=models.RESTRICT)
    movie_details = models.ForeignKey(Movie_Details, on_delete=models.RESTRICT)