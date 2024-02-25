from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from wanimein.api.models import (Genre, Country, Movie_Genre, Movie_Details, Movie_Info, Movie_Actors,
                                 Comment, Actors, Year, User, Episode, Collection, Types, Tag, Movie_Tags)


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Genre.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Country.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class YearSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Year
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Year.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_InfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    remark = serializers.CharField(max_length=255, allow_null=True)
    picture = serializers.CharField()
    type = serializers.IntegerField()
    country = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Country.objects.all())
    year = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Year.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Info
        fields = (
            'id',
            'name',
            'remark',
            'picture',
            'type',
            'country',
            'year',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Info.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.type = validated_data.get('type', instance.type)
        instance.country = validated_data.get('country', instance.country)
        instance.year = validated_data.get('year', instance.year)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_GenreSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Genre.objects.all())
    genre_name = serializers.StringRelatedField(source='genre', read_only=True)
    movie_info = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Movie_Info.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Genre
        fields = (
            'id',
            'genre',
            'genre_name',
            'movie_info',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Genre.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.genre = validated_data.get('genre', instance.genre)
        instance.movie_info = validated_data.get('movie_info', instance.movie_info)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    ip = serializers.CharField(max_length=255)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = User
        fields = (
            'id',
            'login',
            'password',
            'ip',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['token'] = instance.token

        return representation


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    author_name = serializers.StringRelatedField(source='author', read_only=True)
    respondent = serializers.IntegerField(allow_null=True)
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                       queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'author_name',
            'respondent',
            'movie_details',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.author = validated_data.get('author', instance.author)
        instance.respondent = validated_data.get('respondent', instance.author)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class ActorsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    people = serializers.BooleanField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Actors
        fields = (
            'id',
            'name',
            'people',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Actors.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.people = validated_data.get('people', instance.people)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_DetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    picture = serializers.CharField()
    language = serializers.CharField()
    all_episodes = serializers.IntegerField()
    current_episodes = serializers.IntegerField()
    director = serializers.CharField()
    last_episode = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    synopsis = serializers.CharField()
    country = serializers.StringRelatedField(many=False)
    year = serializers.StringRelatedField(many=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Details
        fields = (
            'id',
            'name',
            'picture',
            'language',
            'all_episodes',
            'current_episodes',
            'director',
            'last_episode',
            'synopsis',
            'country',
            'year',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Details.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.language = validated_data.get('language', instance.language)
        instance.all_episodes = validated_data.get('all_episodes', instance.all_episodes)
        instance.current_episodes = validated_data.get('current_episodes', instance.current_episodes)
        instance.director = validated_data.get('director', instance.director)
        instance.last_episode = validated_data.get('last_episode', instance.last_episode)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        instance.country = validated_data.get('country', instance.country)
        instance.year = validated_data.get('year', instance.year)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['episodes'] = (Episode.objects.filter(movie_details=representation['id'])
                                      .values('id', 'name', 'url').order_by('id'))
        # representation['tags'] = (Movie_Tags.objects.filter(movie_details=representation['id'])
        #                           .values('id', 'tags').order_by('id'))

        return representation

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_ActorsSerializer(serializers.ModelSerializer):
    actor = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Actors.objects.all())
    actor_name = serializers.StringRelatedField(source='actor', read_only=True)
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                       queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Actors
        fields = (
            'id',
            'movie_details',
            'actor',
            'actor_name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Actors.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.movie_details = validated_data.get('movie_details', instance.movie_details)
        instance.actor = validated_data.get('actor', instance.actor)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class EpisodeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    url = serializers.CharField()
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                       queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Episode
        fields = (
            'id',
            'name',
            'url',
            'movie_details',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Episode.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                       queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Collection
        fields = (
            'id',
            'user',
            'movie_details',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Collection.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.movie_details = validated_data.get('movie_details', instance.movie_details)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TypesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Types
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Types.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Tag.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_TagsSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Tag.objects.all())
    tags_name = serializers.StringRelatedField(source='tags', read_only=True)
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                       queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Tags
        fields = (
            'id',
            'tags',
            'tags_name',
            'movie_details',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Tags.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
        # instance.genre = validated_data.get('genre', instance.genre)
        # instance.movie_info = validated_data.get('movie_info', instance.movie_info)
        # instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        return instance

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['episodes'] = (Episode.objects.filter(movie_details=representation['id'])
    #                                   .values('id', 'name', 'url').order_by('id'))
    #     # representation['tags'] = (Movie_Tags.objects.filter(movie_details=representation['id'])
    #     #                           .values('id', 'tags').order_by('id'))
    #
    #     return representation

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()
