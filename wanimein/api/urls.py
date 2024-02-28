from django.urls import re_path, path

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
        'get': 'get',
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
    re_path('movie_actor', views.Movie_ActorsView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('movie_genr', views.Movie_GenreView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    path('episode', views.EpisodeView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    re_path('collection', views.CollectionView.as_view({
        'get': 'list',
        'put': 'new',
        'post': 'remove'
    })),
    path('check', views.CheckCollectionView.as_view({
        'get': 'check_collect'
    })),
    re_path('types', views.TypesView.as_view({
        'get': 'list',
        'put': 'new'
    })),
    path('auth', views.UserView.as_view(), name='user'),
    path('tag', views.TagView.as_view({
        'get': 'list',
        'put': 'new'
    }), name='tag'),
    path('movie_tags', views.Movie_TagsView.as_view({
        'get': 'getting',
        'put': 'new'
    }), name='movie_tag'),
    path('movie_ratings', views.Movie_RatingsView.as_view({
        'get': 'get',
        'put': 'new'
    }), name='movie_tag'),
    path('save_views', views.save_views, name='save_views'),
    path('episode_view', views.Episode_ViewView.as_view({
        'get': 'get',
        'put': 'new'
    }), name='episode_view'),
]
