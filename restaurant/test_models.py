from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = str(item)
        self.assertEqual(itemstr, "IceCream ($80)")
        self.assertEqual(item.inventory, 100)