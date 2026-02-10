"""
Django management command to populate the Menu table with sample data.

Usage:
    python manage.py populate_menu
    python manage.py populate_menu --clear  # Clear existing items first
"""

from django.core.management.base import BaseCommand
from restaurant.models import Menu
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populates the Menu table with sample menu items'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing menu items before populating',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing menu items...')
            Menu.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared all menu items.'))

        # Sample menu items based on Mediterranean cuisine
        menu_items = [
            {
                'title': 'Greek Salad',
                'price': Decimal('12.99'),
                'inventory': 50
            },
            {
                'title': 'Bruschetta',
                'price': Decimal('8.99'),
                'inventory': 40
            },
            {
                'title': 'Grilled Fish',
                'price': Decimal('18.99'),
                'inventory': 30
            },
            {
                'title': 'Pasta Carbonara',
                'price': Decimal('14.99'),
                'inventory': 45
            },
            {
                'title': 'Lemon Dessert',
                'price': Decimal('6.99'),
                'inventory': 60
            },
            {
                'title': 'Mediterranean Pizza',
                'price': Decimal('16.99'),
                'inventory': 35
            },
            {
                'title': 'Lamb Kebab',
                'price': Decimal('19.99'),
                'inventory': 25
            },
            {
                'title': 'Hummus & Pita',
                'price': Decimal('7.99'),
                'inventory': 55
            },
            {
                'title': 'Moussaka',
                'price': Decimal('17.99'),
                'inventory': 20
            },
            {
                'title': 'Baklava',
                'price': Decimal('5.99'),
                'inventory': 50
            },
            {
                'title': 'Chicken Souvlaki',
                'price': Decimal('15.99'),
                'inventory': 40
            },
            {
                'title': 'Spanakopita',
                'price': Decimal('9.99'),
                'inventory': 35
            },
            {
                'title': 'Seafood Risotto',
                'price': Decimal('21.99'),
                'inventory': 15
            },
            {
                'title': 'Tiramisu',
                'price': Decimal('7.99'),
                'inventory': 45
            },
            {
                'title': 'Turkish Delight',
                'price': Decimal('4.99'),
                'inventory': 70
            },
        ]

        created_count = 0
        updated_count = 0

        for item_data in menu_items:
            item, created = Menu.objects.get_or_create(
                title=item_data['title'],
                defaults={
                    'price': item_data['price'],
                    'inventory': item_data['inventory']
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {item.title} - ${item.price}')
                )
            else:
                # Update existing item if it exists
                item.price = item_data['price']
                item.inventory = item_data['inventory']
                item.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated: {item.title} - ${item.price}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully populated menu! '
                f'Created: {created_count}, Updated: {updated_count}, '
                f'Total items: {Menu.objects.count()}'
            )
        )

