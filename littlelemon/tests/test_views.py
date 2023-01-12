from django.test import TestCase
import json
from restaurant.models import Menu
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):
    def setUp(cls):
        number_of_menus = 20
        for menu_id in range(number_of_menus):
            Menu.objects.create(
                title=f"Menu item {menu_id}",
                price=f"{menu_id * 2}",
                inventory=f"{menu_id * 3}",
            )

    def test_get_all(self):
        response = self.client.get("/restaurant/menu/")
        menus = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(menus), 20)
