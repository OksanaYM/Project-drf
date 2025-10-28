from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from core.dataclasses.user_dataclass import User

from apps.pizza.models import PizzaModel
from apps.pizza_shop.models import PizzaShopModel

UserModel = get_user_model()

class PizzaAPITestCase(APITestCase):
    def setUp(self):
        pizza_shop = PizzaShopModel.objects.create(
            name='Pizza Shop'
        )
        self.pizza_one = PizzaModel.objects.create(
            name = 'Pizza_one',
            size = 20,
            price = 300,
            day= 'Monday',
            pizza_shop=pizza_shop
        )
        self.pizza_two = PizzaModel.objects.create(
            name='Pizza_two',
            size=20,
            price=300,
            day='Monday',
            pizza_shop=pizza_shop
        )

    def _authenticate(self):
        user: User = UserModel.objects.create_user(
            email='admin@gmail.com',
            password='admin'
        )
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'),
                               {
                                   'email': user.email,
                                   'password': 'admin'
                                })
        print(res.data, '!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + res.data['access'])

    def test_get_all_pizzas(self):
        res = self.client.get(reverse('pizza_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['data']), 2)
        pizza_names = list(reversed(['Pizza_one', 'Pizza_two']))
        for i, pizza in enumerate(PizzaModel.objects.all()):
            self.assertEqual(pizza.name, pizza_names[i])

    def test_create_pizza_without_auth(self):
        count_before = PizzaModel.objects.count()
        res = self.client.post(reverse('pizza_list_create'),
                               data={
                                   'name': 'Pizza_no_auth',
                                   'size': 20,
                                   'price': 200,
                                   'day': 'Monday'
                               })
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 0)

    def test_create_pizza_with_auth(self):
        self._authenticate()
        count_before = PizzaModel.objects.count()
        res = self.client.post(reverse('pizza_list_create'),
                               data={
                                   'name': 'Classic',
                                   'size': 20,
                                   'price': 250,
                                   'day': 'Monday'
                               })
        print(res.data, '*********************')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        count_after = PizzaModel.objects.count()
        self.assertEqual(count_after - count_before, 1)
        self.assertEqual(res.data['name'], 'Classic')

