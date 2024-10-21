from django.core.management.base import BaseCommand
from faker import Faker
from todo.models import ToDo
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Generate fake to-do items and users"

    def add_arguments(self, parser):
        parser.add_argument("num_users", type=int, help="Number of users to create")
        parser.add_argument("num_items", type=int, help="Number of to-do items to create")

    def handle(self, *args, **kwargs):
        num_users = kwargs["num_users"]
        num_items = kwargs["num_items"]
        fake = Faker()

        # Create fake users
        users = []
        for _ in range(num_users):
            user = User(username=fake.user_name(), email=fake.email())
            user.set_password("password")  # Set a default password
            user.save()
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: "{user.username}"'))

        # Generate fake to-do items
        for _ in range(num_items):
            title = fake.sentence(nb_words=6)
            description = fake.paragraph(nb_sentences=3)
            completed = random.choice([True, False])
            owner = random.choice(users)

            todo = ToDo(title=title, description=description, completed=completed, owner=owner)
            todo.save()
            self.stdout.write(self.style.SUCCESS(f'Created to-do: "{todo.title}"'))
