from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from drf_yasg.utils import swagger_auto_schema

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializer import PizzaPhotoSerializer, PizzaResponseSerializer, PizzaSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
        operation_description='PIZZA',
        responses={200: PizzaResponseSerializer()},
        operation_summary='get all pizzas'
    )
)
class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)



class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']

class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny, )

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)

