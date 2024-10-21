import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from your_app.models import Blog, Dislike


class Command(BaseCommand):
    help = "Generate fake dislikes"

    def add_arguments(self, parser):
        parser.add_argument("--num-dislikes", type=int, default=50, help="Number of dislikes to create (default: 50)")

    def handle(self, *args, **options):
        num_dislikes = options["num_dislikes"]
        User = get_user_model()
        users = list(User.objects.all())
        blogs = list(Blog.objects.all())

        for _ in range(num_dislikes):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found!"))
                return

            Dislike.objects.create(blog=random.choice(blogs), owner=random.choice(users))

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_dislikes} dislikes!"))
