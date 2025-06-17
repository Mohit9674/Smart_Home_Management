from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create initial superuser if not exists'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'mohit9674'
        email = 'mohitnotani52@gmail.com'
        password = 'Mohit@9674'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))
