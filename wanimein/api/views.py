from rest_framework import mixins, viewsets

from wanimein.api.models import Movie_Info, Genre, Country, Comment, Movie_Genre, Movie_Details, Movie_Actors, \
    Collection, Actors, Year, Episode
from wanimein.api.serializers import Movie_InfoSerializer, Movie_DetailsSerializer, Movie_ActorsSerializer, \
    Movie_GenreSerializer, GenreSerializer, CommentSerializer, CountrySerializer, CollectionSerializer, \
    EpisodeSerializer, ActorsSerializer, UserSerializer, YearSerializer


class MovieView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = Movie_InfoSerializer
    queryset = Movie_Info.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        m_type = self.request.query_params.get('type', None)
        year = self.request.query_params.get('year', None)
        country = self.request.query_params.get('country', None)
        name = self.request.query_params.get('name', None)
        if m_type is not None:
            queryset = queryset.filter(type=m_type)
        if year is not None:
            queryset = queryset.filter(year=year)
        if country is not None:
            queryset = queryset.filter(country=country)
        if name is not None:
            queryset = queryset.filter(name=name)

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenreView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class YearView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = YearSerializer
    queryset = Year.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CountryView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_DetailsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = Movie_DetailsSerializer
    queryset = Movie_Details.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_GenreView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = Movie_GenreSerializer
    queryset = Movie_Genre.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ActorsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = ActorsSerializer
    queryset = Actors.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Movie_ActorsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = Movie_ActorsSerializer
    queryset = Movie_Actors.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EpisodeView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CollectionView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'slug'
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)