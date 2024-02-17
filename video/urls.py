from django.urls import path

from video import views

urlpatterns = [
    path('video_stream/<str:filename>/', views.video_stream, name='video_stream'),
    path('video_stream/<str:filename>/<str:player>/', views.video_segment, name='video_stream_with_player'),
    path('make_hls/<str:filename>/', views.make_hls, name='video_stream_with_player'),
]
