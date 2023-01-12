from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title="Ice Cream", price=5, inventory=30)
        item = item.get_item()
        self.assertEqual(item, "Ice Cream: 5")
