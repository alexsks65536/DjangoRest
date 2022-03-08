from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        User.objects.create_superuser('admin', 'admin@geekshop.local', 'geekbrains')
        User.objects.create_superuser('alex', 'alexsks@geekshop.local', 'geekbrains')
        User.objects.create_user('username', 'myemail@crazymail.com', 'geekbrains')
        User.objects.create_user('user', 'user@crazymail.com', 'geekbrains')
        User.objects.create_user('djangouser', 'myemail@crazymail.com', 'geekbrains')
        User.objects.create_user('leo', 'leomyemail@crazymail.com', 'geekbrains')
        User.objects.create_user('john', 'johnmyemail@crazymail.com', 'geekbrains')
        User.objects.create_user('mark', 'markmyemail@crazymail.com', 'geekbrains')
        User.objects.create_user('timaty', 'blackstar@crazymail.com', 'geekbrains')
