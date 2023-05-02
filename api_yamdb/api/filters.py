import django_filters
from rest_framework import mixins, viewsets
from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',
                                     lookup_expr='icontains'
                                     )

    category = django_filters.CharFilter(field_name='category__slug',
                                         lookup_expr='icontains'
                                         )
    genre = django_filters.CharFilter(field_name='genre__slug',
                                      lookup_expr='icontains'
                                      )
    year = django_filters.CharFilter(field_name='year',
                                     lookup_expr='icontains'
                                     )

    class Meta:
        model = Title
        fields = '__all__'


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass
