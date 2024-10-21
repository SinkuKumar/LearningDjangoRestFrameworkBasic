import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from your_app.models import Blog


class Command(BaseCommand):
    help = "Generate fake blogs"

    def add_arguments(self, parser):
        parser.add_argument("--num-blogs", type=int, default=20, help="Number of blogs to create (default: 20)")

    def handle(self, *args, **options):
        num_blogs = options["num_blogs"]
        fake = Faker()
        User = get_user_model()
        users = list(User.objects.all())

        for _ in range(num_blogs):
            if not users:
                self.stdout.write(self.style.WARNING("No users found!"))
                return

            blog = Blog.objects.create(title=fake.sentence(nb_words=6), content=fake.text(), owner=random.choice(users))
            self.stdout.write(f"Created blog: {blog.title}")

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_blogs} blogs!"))
