from rest_framework import mixins, viewsets

from wanimein.api.models import Movie_Info


class MovieView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet, mixins.DestroyModelMixin):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    # serializer_class = ArticleSerializer
    queryset = Movie_Info.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__articles=category)

        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
