import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from your_app.models import Blog, Comment, Like, Dislike


class Command(BaseCommand):
    help = "Generate fake data for Blog, Comment, Like, and Dislike models"

    def add_arguments(self, parser):
        parser.add_argument("--num-blogs", type=int, default=20, help="Number of blogs to create (default: 20)")

    def handle(self, *args, **options):
        num_blogs = options["num_blogs"]
        fake = Faker()
        User = get_user_model()

        # Create some users
        users = [User.objects.create_user(username=fake.user_name(), password="password") for _ in range(10)]

        # Create fake blogs
        for _ in range(num_blogs):
            blog = Blog.objects.create(title=fake.sentence(nb_words=6), content=fake.text(), owner=random.choice(users))
            self.stdout.write(f"Created blog: {blog.title}")

            # Create fake comments for each blog
            for _ in range(random.randint(1, 5)):
                Comment.objects.create(blog=blog, content=fake.text(max_nb_chars=200), owner=random.choice(users))

            # Create likes and dislikes for each blog
            for user in users:
                if random.choice([True, False]):
                    Like.objects.create(blog=blog, owner=user)
                    self.stdout.write(f"User {user.username} liked blog: {blog.title}")

                if random.choice([True, False]):
                    Dislike.objects.create(blog=blog, owner=user)
                    self.stdout.write(f"User {user.username} disliked blog: {blog.title}")

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_blogs} blogs!"))
