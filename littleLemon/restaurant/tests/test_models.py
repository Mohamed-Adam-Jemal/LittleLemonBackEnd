from django.test import TestCase
from restaurant.models import Menu

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a Menu item
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Assert that the string representation of the item is correct
        self.assertEqual(str(item), "IceCream : 80")
