from django.urls import re_path

from wanimein.api import views

urlpatterns = [
    re_path('movie_info/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('year/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('country/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('genre/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('movie_details/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('user/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('comment/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('actors/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('movie_actors/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('movie_genre/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('episode/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
    re_path('collection/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
]
