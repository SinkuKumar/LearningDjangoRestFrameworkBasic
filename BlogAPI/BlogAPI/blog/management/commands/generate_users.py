from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Generate fake users"

    def add_arguments(self, parser):
        parser.add_argument("--num-users", type=int, default=10, help="Number of users to create (default: 10)")

    def handle(self, *args, **options):
        num_users = options["num_users"]
        fake = Faker()
        User = get_user_model()

        for _ in range(num_users):
            user = User.objects.create_user(username=fake.user_name(), password="password")
            self.stdout.write(f"Created user: {user.username}")

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_users} users!"))
