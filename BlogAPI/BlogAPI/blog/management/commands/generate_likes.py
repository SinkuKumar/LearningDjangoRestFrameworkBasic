import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from your_app.models import Blog, Like


class Command(BaseCommand):
    help = "Generate fake likes"

    def add_arguments(self, parser):
        parser.add_argument("--num-likes", type=int, default=100, help="Number of likes to create (default: 100)")

    def handle(self, *args, **options):
        num_likes = options["num_likes"]
        User = get_user_model()
        users = list(User.objects.all())
        blogs = list(Blog.objects.all())

        for _ in range(num_likes):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found!"))
                return

            Like.objects.create(blog=random.choice(blogs), owner=random.choice(users))

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_likes} likes!"))
