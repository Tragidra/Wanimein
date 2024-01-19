from rest_framework import serializers

from wanimein.api.models import (Genre, Country, Movie_Genre, Movie_Details, Movie_Info, Movie_Actors,
                                 Movie_Actors, Movie_Info, Comment, Actors, Year)


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
        model = Genre
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
        model = Genre
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
    picture = serializers.CharField()
    type = serializers.IntegerField()
    country = serializers.IntegerField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
            'picture',
            'type',
            'country',
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