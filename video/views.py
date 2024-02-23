# views.py

import os
from django.http import JsonResponse, HttpResponse
from .tasks import video_cut

VIDEO_ROOT = r"C:\Users\Krulzifer\PycharmProjects\wanimein\video\source"
out_root_playlist = r"C:\Users\Krulzifer\PycharmProjects\wanimein\video\hls"


def make_hls(request, filename):
    video_cut.delay(filename)
    response = JsonResponse({'status': 'ok'})
    return response


def video_segment(request, filename, player):
    playlist = os.path.join('video', 'hls', os.path.splitext(os.path.basename(filename))[0])
    segment_path = os.path.join(playlist, f'{player}')

    # Возвращаем содержимое сегмента
    with open(segment_path, 'rb') as segment_file:
        response = HttpResponse(segment_file.read(), content_type='video/mp2t')
    return response


def video_stream(request, filename):
    player = os.path.join('video', 'hls', os.path.splitext(os.path.basename(filename))[0],
                          os.path.splitext(os.path.basename(filename))[0]+'.m3u8')
    with open(player, 'r') as playlist_file:
        playlist_content = playlist_file.read()

    response = HttpResponse(playlist_content, content_type='application/vnd.apple.mpegurl')
    return response
