from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from backend.apps.pizza.filter import PizzaFilter
from backend.apps.pizza.models import PizzaModel
from backend.apps.pizza.serializer import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter



class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']
