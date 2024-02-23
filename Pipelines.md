celery -A wanimein flower
celery -A wanimein flower --persistent=True
celery -A wanimein worker -l info
celery -A wanimein worker -l info --pool=solo
docker-compose up -d
 docker-compose stop/down