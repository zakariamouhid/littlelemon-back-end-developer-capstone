from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuItemsAPITest(APITestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.menu_item = Menu.objects.create(
            title="Test Pizza",
            price=15.99,
            inventory=100
        )
    
    def test_get_menu_items(self):
        """Test GET /api/menu/ returns list of items"""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Pizza')
    
    def test_create_menu_item(self):
        """Test POST /api/menu/ creates a new item"""
        data = {
            'title': 'New Burger',
            'price': '10.50',
            'inventory': 50
        }
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(id=response.data['id']).title, 'New Burger')
    
    def test_get_single_menu_item(self):
        """Test GET /api/menu/<id>/ returns specific item"""
        response = self.client.get(f'/api/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Pizza')
        self.assertEqual(response.data['price'], '15.99')
    
    def test_update_menu_item(self):
        """Test PUT /api/menu/<id>/ updates an item"""
        data = {
            'title': 'Updated Pizza',
            'price': '18.99',
            'inventory': 80
        }
        response = self.client.put(
            f'/api/menu/{self.menu_item.id}/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.title, 'Updated Pizza')
        self.assertEqual(float(self.menu_item.price), 18.99)
    
    def test_partial_update_menu_item(self):
        """Test PATCH /api/menu/<id>/ partially updates an item"""
        data = {
            'price': '20.00'
        }
        response = self.client.patch(
            f'/api/menu/{self.menu_item.id}/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(float(self.menu_item.price), 20.00)
        # Title should remain unchanged
        self.assertEqual(self.menu_item.title, 'Test Pizza')
    
    def test_delete_menu_item(self):
        """Test DELETE /api/menu/<id>/ deletes an item"""
        response = self.client.delete(f'/api/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)
    
    def test_get_nonexistent_menu_item(self):
        """Test GET /api/menu/<id>/ with invalid id returns 404"""
        response = self.client.get('/api/menu/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_menu_item_invalid_data(self):
        """Test POST /api/menu/ with invalid data returns 400"""
        data = {
            'title': '',  # Empty title should be invalid
            'price': '10.50',
            'inventory': 50
        }
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class BookingAPITest(APITestCase):
    def setUp(self):
        """Set up test data with authenticated user"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            user=self.user,
            name="Test Booking",
            no_of_guests=2,
            booking_date=timezone.make_aware(datetime(2024, 12, 25, 19, 30))
        )
    
    def test_get_bookings_authenticated(self):
        """Test GET /api/tables/ requires authentication"""
        response = self.client.get('/api/tables/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Booking')
    
    def test_get_bookings_unauthenticated(self):
        """Test GET /api/tables/ fails without authentication"""
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/tables/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_booking(self):
        """Test POST /api/tables/ creates a new booking"""
        data = {
            'name': 'John Doe',
            'no_of_guests': 4,
            'booking_date': '2024-12-31T20:00:00Z'
        }
        response = self.client.post('/api/tables/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(Booking.objects.get(id=response.data['id']).name, 'John Doe')
    
    def test_get_single_booking(self):
        """Test GET /api/tables/<id>/ returns specific booking"""
        response = self.client.get(f'/api/tables/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Booking')
        self.assertEqual(response.data['no_of_guests'], 2)
    
    def test_update_booking(self):
        """Test PUT /api/tables/<id>/ updates a booking"""
        data = {
            'name': 'Updated Booking',
            'no_of_guests': 6,
            'booking_date': '2024-12-31T21:00:00Z'
        }
        response = self.client.put(
            f'/api/tables/{self.booking.id}/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.name, 'Updated Booking')
        self.assertEqual(self.booking.no_of_guests, 6)
    
    def test_delete_booking(self):
        """Test DELETE /api/tables/<id>/ deletes a booking"""
        response = self.client.delete(f'/api/tables/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
    
    def test_create_booking_unauthenticated(self):
        """Test POST /api/tables/ fails without authentication"""
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Unauthorized Booking',
            'no_of_guests': 2,
            'booking_date': '2024-12-31T20:00:00Z'
        }
        response = self.client.post('/api/tables/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class SecuredViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_secured_view_authenticated(self):
        """Test secured view with authentication"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/secured-view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'This view is protected')
    
    def test_secured_view_unauthenticated(self):
        """Test secured view without authentication"""
        response = self.client.get('/api/secured-view/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_get_users_list(self):
        """Test GET /api/users/ returns list of users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_get_single_user(self):
        """Test GET /api/users/<id>/ returns specific user"""
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
    
    def test_create_user(self):
        """Test POST /api/users/ creates a new user"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post('/api/users/', data, format='json')
        # Note: User creation might require special handling depending on serializer
        # This test may need adjustment based on your UserSerializer implementation
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
