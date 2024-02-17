# views.py

import os
import mimetypes
import subprocess
from django.http import StreamingHttpResponse, HttpResponseNotFound, JsonResponse, HttpResponse

VIDEO_ROOT = r"C:\Users\Krulzifer\PycharmProjects\wanimein\video\source"
out_root_playlist = r"C:\Users\Krulzifer\PycharmProjects\wanimein\video\hls"


def make_hls(request, filename):
    file = os.path.splitext(os.path.basename(filename))[0]
    video_file_path = os.path.join(VIDEO_ROOT, filename)
    input_file_path = os.path.join(video_file_path)
    out_root_player = os.path.join('video', 'hls', file, file+'.m3u8')
    # Создаем директорию для хранения HLS-потока
    os.makedirs(os.path.join('video', 'hls', file), exist_ok=True)

    # Запускаем ffmpeg для создания HLS-потока
    cmd = [
        'ffmpeg',
        '-i', input_file_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-f', 'hls',
        '-hls_time', '5',
        '-hls_list_size', '0',
        '-start_number', '1',
        out_root_player
    ]

    subprocess.run(cmd, shell=True)

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
