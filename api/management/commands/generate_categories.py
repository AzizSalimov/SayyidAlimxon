from django.core.management.base import BaseCommand
from api.models import Category
from faker import Faker


class Command(BaseCommand):
    help = 'Populate categories with fake data'

    def handle(self, *args, **options):
        fake = Faker()
        quantity = 10000      # Adjust the quantity as per your needs

        for _ in range(quantity):
            category_name = fake.word()
            category = Category(name=category_name)
            category.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {quantity} categories.'))

