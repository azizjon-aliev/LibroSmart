from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options) -> None:
        from django.contrib.auth.models import User

        if not User.objects.filter(username='admin').exists():
            print("[INFO] Creating superuser...")
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin',
            )
            print("[INFO] Superuser created.")

        else:
            print("[INFO] Superuser already exists.")
