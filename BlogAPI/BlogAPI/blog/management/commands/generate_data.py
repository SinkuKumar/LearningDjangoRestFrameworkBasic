from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from blog.models import Blog, Comment, Like, Dislike
import random


class Command(BaseCommand):
    help = "Generate fake users, blogs, comments, likes, and dislikes"

    def add_arguments(self, parser):
        parser.add_argument("--num-users", type=int, default=10, help="Number of users to create (default: 10)")
        parser.add_argument("--num-blogs", type=int, default=20, help="Number of blogs to create (default: 50)")
        parser.add_argument("--num-comments", type=int, default=50, help="Number of comments to create (default: 100)")
        parser.add_argument("--num-likes", type=int, default=100, help="Number of likes to create (default: 150)")
        parser.add_argument("--num-dislikes", type=int, default=50, help="Number of dislikes to create (default: 50)")

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()

        # Create users
        users = []
        num_users = options["num_users"]
        for _ in range(num_users):
            user = User.objects.create_user(username=fake.user_name(), password="password")
            users.append(user)
            self.stdout.write(f"Created user: {user.username}")

        # Create blogs
        blogs = []
        num_blogs = options["num_blogs"]
        for _ in range(num_blogs):
            if not users:
                self.stdout.write(self.style.WARNING("No users found to create blogs!"))
                return

            blog = Blog.objects.create(title=fake.sentence(nb_words=6), content=fake.text(), owner=random.choice(users))
            blogs.append(blog)
            self.stdout.write(f"Created blog: {blog.title}")

        # Create comments
        num_comments = options["num_comments"]
        for _ in range(num_comments):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found to create comments!"))
                return

            comment = Comment.objects.create(blog=random.choice(blogs), content=fake.text(max_nb_chars=200), owner=random.choice(users))
            self.stdout.write(f"Created comment on blog: {comment.blog.title}")

        # Create likes
        num_likes = options["num_likes"]
        for _ in range(num_likes):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found to create likes!"))
                return

            Like.objects.create(blog=random.choice(blogs), owner=random.choice(users))
            self.stdout.write(f"Created like on a blog")

        # Create dislikes
        num_dislikes = options["num_dislikes"]
        for _ in range(num_dislikes):
            if not blogs or not users:
                self.stdout.write(self.style.WARNING("No blogs or users found to create dislikes!"))
                return

            Dislike.objects.create(blog=random.choice(blogs), owner=random.choice(users))
            self.stdout.write(f"Created dislike on a blog")

        self.stdout.write(self.style.SUCCESS("Successfully generated all data!"))
