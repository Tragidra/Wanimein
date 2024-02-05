from django.urls import re_path

from wanimein.api import views

urlpatterns = [
    re_path('movie_info', views.MovieView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('year', views.YearView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('country', views.CountryView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('genre', views.GenreView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('movie_details', views.Movie_DetailsView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('user', views.Movie_DetailsView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('comment', views.CommentView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('actors', views.ActorsView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('movie_actors', views.Movie_ActorsView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('movie_genr', views.Movie_GenreView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('episode', views.EpisodeView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('collection', views.CollectionView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('types', views.TypesView.as_view({
        'get': 'list',
        'put': 'new'
    })),
]
