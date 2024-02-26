from django.core.cache import cache
from django.db.backends.signals import connection_created
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from wanimein.api.models import Movie_Details


@receiver(connection_created)
def populate_cache(sender, connection, **kwargs):
    if not hasattr(populate_cache, '_has_run'):
        views = Movie_Details.objects.values('name', 'views').order_by('id')
        for i in range(len(views)):
            cache.set(views[i]['name'] + '.views', views[i]['views'])

        setattr(populate_cache, '_has_run', True)
