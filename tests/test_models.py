from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User  # Import User model
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
# TestCase class
from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a MenuItem instance
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        # Test the get_item method's output
        expected_value = "IceCream : 80.00"  # The expected string representation
        self.assertEqual(item.get_item(), expected_value)

class MenuViewTest(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)  # Create a token for the user

        # Create test instances of the MenuItem model
        MenuItem.objects.create(title="Pizza", price=10.00, inventory=5)
        MenuItem.objects.create(title="Burger", price=8.50, inventory=3)

    def test_get_all(self):
        # Set the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        url = reverse('menu-items-list')  # Use the correct name for your URL
        response = self.client.get(url)
        
        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the response data is correct (you can adjust this according to your serializer)
        self.assertEqual(len(response.data), 2)  # Assuming you created 2 MenuItem instances