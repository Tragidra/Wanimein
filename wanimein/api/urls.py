from django.urls import re_path

from wanimein.api import views

urlpatterns = [
    re_path('articles/', views.MovieView.as_view({
        'get': 'list',
        'put': 'create'
    })),
]
