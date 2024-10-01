from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title="Greek Salad", price=12.50, inventory=20)
        self.menu_item2 = Menu.objects.create(title="Grilled Burrito", price=10.00, inventory=15)
        self.menu_item3 = Menu.objects.create(title="Chicken Wings", price=8.00, inventory=10)

        self.client = APIClient()

        # Set the token for authentication
        self.token = '47bff64407c2f0338259512e56571c83e2577689'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_getall(self):
        # Send a GET request to the menu endpoint
        response = self.client.get(reverse('menu-list'))  # Updated to match the new name

        # Get all Menu objects and serialize them
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data matches the response data
        self.assertEqual(response.data, serializer.data)
