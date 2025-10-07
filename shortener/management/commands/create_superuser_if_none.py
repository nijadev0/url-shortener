from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a superuser if none exists"

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
            return

        username = "admin"
        email = "admin@example.com"
        password = "admin"

        User.objects.create_superuser(username=username, email=email, password=password)

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser created successfully!\n"
                f"Username: {username}\n"
                f"Password: {password}\n"
                f"Access admin at: http://localhost:8000/admin/"
            )
        )
