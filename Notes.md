1. При создании моделей db_table = '' нужно для создания моделей с нормальными 
именами.
2. ordering - порядок получения записей, ordering = ["id"]
3. https://testdriven.io/blog/drf-serializers/ - полезная информация о методах
сериализаторов.
4. Если фильтров много - задействуй:

    ```
   def filter_queryset(self, queryset):
     filter_backends = [CategoryFilter]

     if 'geo_route' in self.request.query_params:
        filter_backends = [GeoRouteFilter, CategoryFilter]
     elif 'geo_point' in self.request.query_params:
        filter_backends = [GeoPointFilter, CategoryFilter]

     for backend in list(filter_backends):
        queryset = backend().filter_queryset(self.request, queryset, view=self)

     return queryset
   ```
5. Если при нажатии на эпизод выскакивает ошибка о неопределённости 
версии - в библиотеке не указана версия, поправить там же