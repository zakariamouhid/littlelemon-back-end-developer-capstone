from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuTest(TestCase):
    def test_menu_item_creation_str_and_inventory(self):
        """Test menu item creation, string representation, and inventory field"""
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = str(item)
        self.assertEqual(itemstr, "IceCream ($80)")
        self.assertEqual(item.inventory, 100)
    
    def test_menu_item_creation(self):
        """Test creating a menu item with all fields"""
        item = Menu.objects.create(
            title="Pizza",
            price=12.50,
            inventory=50
        )
        self.assertEqual(item.title, "Pizza")
        self.assertEqual(float(item.price), 12.50)
        self.assertEqual(item.inventory, 50)
    
    def test_menu_item_str_representation(self):
        """Test the string representation of MenuItem"""
        item = Menu.objects.create(title="Burger", price=9.99, inventory=30)
        self.assertEqual(str(item), "Burger ($9.99)")
    
    def test_menu_item_decimal_price(self):
        """Test that price can handle decimal values correctly"""
        item = Menu.objects.create(title="Salad", price=7.50, inventory=25)
        self.assertEqual(float(item.price), 7.50)

class BookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")

    def test_booking_creation(self):
        """Test creating a booking"""
        booking = Booking.objects.create(
            user=self.user,
            name="John Doe",
            no_of_guests=4,
            booking_date=timezone.make_aware(datetime(2024, 12, 25, 19, 30))
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertIn("John Doe", str(booking))
        self.assertIn("4", str(booking))
    
    def test_booking_str_representation(self):
        """Test the string representation of Booking"""
        booking = Booking.objects.create(
            user=self.user,
            name="Jane Smith",
            no_of_guests=2,
            booking_date=timezone.make_aware(datetime(2024, 12, 31, 20, 0))
        )
        booking_str = str(booking)
        self.assertIn("Jane Smith", booking_str)
        self.assertIn("2024-12-31", booking_str)
        self.assertIn("2", booking_str)
    
    def test_booking_with_different_guest_counts(self):
        """Test bookings with various guest counts"""
        booking1 = Booking.objects.create(
            user=self.user,
            name="Single Guest",
            no_of_guests=1,
            booking_date=timezone.make_aware(datetime(2024, 12, 25, 18, 0))
        )
        booking2 = Booking.objects.create(
            user=self.user,
            name="Large Party",
            no_of_guests=10,
            booking_date=timezone.make_aware(datetime(2024, 12, 25, 19, 0))
        )
        self.assertEqual(booking1.no_of_guests, 1)
        self.assertEqual(booking2.no_of_guests, 10)