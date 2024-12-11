from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Функция для создания суперпользователя. """
        user = User.objects.create(
            email='test@admin.ru',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password('zxc123')
        user.save()
