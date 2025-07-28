from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = [
            'Cozy apartment in Lagos',
            'Beachfront villa in Zanzibar',
            'Cabin in the mountains',
            'Modern studio in Nairobi',
            'Luxury suite in Accra',
        ]
        Listing.objects.all().delete()

        for i in range(5):
            Listing.objects.create(
                title=titles[i],
                description='A lovely place to stay.',
                location='City Center',
                price_per_night=random.randint(50, 300),
                available=True
            )
        self.stdout.write(self.style.SUCCESS('Sample listings created!'))
