import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from your_app.models import Blog, Comment


class Command(BaseCommand):
    help = "Generate fake comments"

    def add_arguments(self, parser):
        parser.add_argument("--num-comments", type=int, default=50, help="Number of comments to create (default: 50)")

    def handle(self, *args, **options):
        num_comments = options["num_comments"]
        fake = Faker()
        User = get_user_model()
        users = list(User.objects.all())
        blogs = list(Blog.objects.all())

        for _ in range(num_comments):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found!"))
                return

            comment = Comment.objects.create(blog=random.choice(blogs), content=fake.text(max_nb_chars=200), owner=random.choice(users))
            self.stdout.write(f"Created comment on blog: {comment.blog.title}")

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_comments} comments!"))
