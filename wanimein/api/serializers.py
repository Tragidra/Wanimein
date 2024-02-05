from rest_framework import serializers

from wanimein.api.models import (Genre, Country, Movie_Genre, Movie_Details, Movie_Info, Movie_Actors,
                                 Movie_Actors, Movie_Info, Comment, Actors, Year, User, Episode, Collection, Types)


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

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_InfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    remark = serializers.CharField(max_length=255)
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

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_GenreSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Genre.objects.all())
    movie_info = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Movie_Info.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Genre
        fields = (
            'id',
            'genre',
            'movie_info',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Genre.objects.create(
            **validated_data
        )

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
        return User.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    respondent = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'respondent',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data
        )

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

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_DetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    picture = serializers.CharField()
    language = serializers.CharField()
    episodes = serializers.IntegerField()
    director = serializers.CharField()
    last_episode = serializers.DateTimeField()
    synopsis = serializers.CharField()
    country = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Country.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Details
        fields = (
            'id',
            'name',
            'picture',
            'language',
            'episodes',
            'director',
            'last_episode',
            'synopsis',
            'country',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Details.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class Movie_ActorsSerializer(serializers.ModelSerializer):
    actor = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Actors.objects.all())
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Movie_Actors
        fields = (
            'id',
            'movie_details',
            'actor',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Movie_Actors.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class EpisodeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Movie_Details.objects.all())
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Episode
        fields = (
            'id',
            'name',
            'createdAt',
            'updatedAt',
        )

    def create(self, validated_data):
        return Episode.objects.create(
            **validated_data
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    movie_details = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Movie_Details.objects.all())
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