from django.test import TestCase
from django.urls import reverse


class RestaurantViewsTest(TestCase):
    def test_index_view_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_view_renders(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_menu_view_renders(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    def test_book_view_renders(self):
        response = self.client.get(reverse("book"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")


