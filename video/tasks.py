import os
import subprocess

from celery import Celery, shared_task
from django.http import JsonResponse

app = Celery('tasks', broker='amqp://master:astrafaz99@localhost:5672')
VIDEO_ROOT = r"C:\Users\Krulzifer\PycharmProjects\wanimein\video\source"


@shared_task()
def video_cut(filename):
    file = os.path.splitext(os.path.basename(filename))[0]
    video_file_path = os.path.join(VIDEO_ROOT, filename)
    input_file_path = os.path.join(video_file_path)
    out_root_player = os.path.join('video', 'hls', file, file + '.m3u8')
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

@shared_task()
def prtintl():
    print('111')