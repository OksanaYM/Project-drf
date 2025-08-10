from django_filters import rest_framework as filters


class PizzaFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')