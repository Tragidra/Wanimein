import jwt
from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.db.models import Value
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, viewsets, generics
from rest_framework.generics import get_object_or_404

from wanimein import settings
from wanimein.api.models import Movie_Info, Genre, Country, Comment, Movie_Genre, Movie_Details, Movie_Actors, \
    Collection, Actors, Year, Episode, Types, User, Tag, Movie_Tags, Movie_Ratings, Episode_View
from wanimein.api.serializers import Movie_InfoSerializer, Movie_DetailsSerializer, Movie_ActorsSerializer, \
    Movie_GenreSerializer, GenreSerializer, CommentSerializer, CountrySerializer, CollectionSerializer, \
    EpisodeSerializer, ActorsSerializer, YearSerializer, TypesSerializer, \
    UserSerializer, TagSerializer, Movie_TagsSerializer, Movie_RatingsSerializer, Episode_ViewSerializer

VIDEO_ROOT = r"C:\Users\Krulzifer\PycharmProjects\wanimein\wanimein\api\source"


class MovieView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = Movie_InfoSerializer
    queryset = Movie_Info.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        m_type = self.request.query_params.get('movtype', None)
        if m_type == '0':
            m_type = None
        year = self.request.query_params.get('year', None)
        country = self.request.query_params.get('country', None)
        name = self.request.query_params.get('keyword', None)
        genre = self.request.query_params.get('genre', None)
        if m_type is not None:
            queryset = queryset.filter(type=m_type)
        if year is not None:
            queryset = queryset.filter(year=year)
        if country is not None:
            queryset = queryset.filter(country=country)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if genre is not None:
            queryset = queryset.filter(movie_genre__genre=genre)

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenreView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by('id')

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class YearView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = YearSerializer
    queryset = Year.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by('id')

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CountryView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by('name')

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_DetailsView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = Movie_DetailsSerializer
    queryset = Movie_Details.objects.all()

    def get_queryset(self):
        mov_id = self.request.query_params.get('vod_id', None)
        request_type = self.request.query_params.get('type', None)
        if request_type is not None:
            queryset = self.queryset.annotate(type=Value(request_type))
            if request_type == 'news':
                queryset = queryset.order_by('updated_at')[:5]
            elif request_type == 'hot':
                queryset = queryset.order_by('id')[:6]
        else:
            queryset = self.queryset.annotate(type=Value('default'))
            queryset = queryset.filter(id=mov_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_GenreView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
    serializer_class = Movie_GenreSerializer
    queryset = Movie_Genre.objects.all()

    def get_queryset(self):
        mov_id = self.request.query_params.get('vod_id', None)
        queryset = self.queryset.filter(movie_info=mov_id)

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        mov_id = self.request.query_params.get('movie_details', None)
        queryset = self.queryset.filter(movie_details_id=mov_id)

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_ActorsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
    serializer_class = Movie_ActorsSerializer
    queryset = Movie_Actors.objects.all()

    def get_queryset(self):
        mov_id = self.request.query_params.get('vod_id', None)
        queryset = self.queryset.filter(movie_details_id=mov_id)

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EpisodeView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CollectionView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
    multiple_lookup_fields = ['user', 'movie_details']
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        movie_detail = self.request.query_params.get('movie_detail', None)
        user = self.request.query_params.get('user', None)
        if movie_detail is not None and user is not None:
            queryset = self.queryset.filter(movie_detail=movie_detail, user=user)
        elif user is not None:
            queryset = self.queryset.filter(user=user)

        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.request.data[field]

        obj = get_object_or_404(queryset, **filter)
        return obj

    def list(self, request):
        serializer_context = {'request': request}
        queryset = self.get_queryset()
        ids = []
        movie_details = queryset.values('movie_details')
        for i in range(len(movie_details)):
            ids.append(movie_details[i]['movie_details'])
        page = self.paginate_queryset(Movie_Info.objects.all().annotate(user=Value(self.request.query_params.get('user', None)))
                                                                  .filter(id__in=ids))
        print(page[0].user)
        serializer = Movie_InfoSerializer(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def remove(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class CheckCollectionView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'id'
    multiple_lookup_fields = ['user', 'movie_details']
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        movie_detail = self.request.query_params.get('movie_detail', None)
        user = self.request.query_params.get('user', None)
        if movie_detail is not None and user is not None:
            queryset = self.queryset.filter(movie_detail=movie_detail, user=user)
        elif user is not None:
            queryset = self.queryset.filter(user=user)

        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.request.query_params[field]

        obj = get_object_or_404(queryset, **filter)
        return obj

    def check_collect(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)


class TypesView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = TypesSerializer
    queryset = Types.objects.all()

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               generics.GenericAPIView, mixins.ListModelMixin):
    lookup_field = 'id'
    multiple_lookup_fields = ['login', 'password']
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        # self.request = self.request.copy()
        token = self.request.query_params.get('token', None)
        if token is not None:
            id = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            queryset = self.queryset.filter(id=id['id'])
        else:
            queryset = self.queryset
        return queryset

    '''Разрешить мутацию при запросах с Постмана'''

    def get_object(self):
        queryset = self.get_queryset()
        # self.request.data._mutable = True
        validation = self.request.data['password'] = check_password(self.request.data['password'],
                                                                    queryset.values('password').first()['password'])
        if validation:
            self.request.data['password'] = queryset.values('password').first()['password']
        # self.request.data._mutable = False
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.request.data[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TagView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
              viewsets.GenericViewSet, mixins.DestroyModelMixin):
    lookup_field = 'name'
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by('id')

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

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie_TagsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin):
    lookup_field = 'id'
    serializer_class = Movie_TagsSerializer
    pagination_class = None
    queryset = Movie_Tags.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        ids = self.request.query_params.get('ids', None)
        if ids is not None:
            ids = ids.split('=')[1]
            ids = [int(id) for id in ids.split(',')]
            queryset = self.queryset.filter(movie_details__in=ids)

        return queryset

    def getting(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@csrf_exempt
def save_views(request):
    if request.method == "POST":
        movie_details = Movie_Details.objects.all()
        for movie_detail in movie_details:
            movie_detail.views = cache.get(movie_detail.name + '.views')
            movie_detail.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'Доступ запрещён'})


class Movie_RatingsView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin):
    lookup_field = 'id'
    serializer_class = Movie_RatingsSerializer
    pagination_class = None
    queryset = Movie_Ratings.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        ids = self.request.query_params.get('ids', None)
        if ids is not None:
            ids = ids.split('=')[1]
            ids = [int(id) for id in ids.split(',')]
            queryset = self.queryset.filter(movie_details__in=ids)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Episode_ViewView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin):
    lookup_field = 'id'
    serializer_class = Episode_ViewSerializer
    pagination_class = None
    queryset = Episode_View.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def new(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)