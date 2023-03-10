from django.core.management.base import BaseCommand
import argparse

# from users.models import User
from django.contrib.auth.models import User as UserType
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from faker import Faker
from django.utils import timezone
from posts.models import Post
import random

fake = Faker("pt_BR")

User: UserType = get_user_model()


class Command(BaseCommand):
    help = "Create random users and posts"

    def add_arguments(self, parser):
        parser.add_argument("num_users", type=int, help="Number of users to be created")
        parser.add_argument("num_posts", type=int, help="Number of posts to be created")

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("seeding data...\n"))

        self.stdout.write(self.style.WARNING("creating users..."))

        # Create a specific user with ID 1
        userFirst = User.objects.create(
            id=1,
            username="João",
            first_name="João",
            last_name="Teste",
            email="joao@teste.com",
            password="1234",
            updated_at=timezone.now(),
        )

        num_users = options["num_users"]
        users = [userFirst]
        for i in range(num_users - 1):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = fake.user_name()
            email = fake.email()
            password = "1234"

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                updated_at=timezone.now(),
            )
            users.append(user)

        self.stdout.write(self.style.SUCCESS(f"{num_users} users created!"))

        self.stdout.write(self.style.WARNING("creating posts..."))

        num_posts = options["num_posts"]
        count = 0
        for i in range(num_posts):
            post_text = fake.paragraph(nb_sentences=10)
            user = random.choice(users)
            is_public = random.choice([True, False])

            post = Post.objects.create(
                text=post_text,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                is_public=is_public,
                user=user,
            )

            count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} posts created!"))
