import json, os

from django.core.management.base import BaseCommand
from users.models import User
from todolist.models import Project, Todo


JSON_PATH = "users/json"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json"), "r") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json("users")


        User.objects.all().delete()
        for user in users:
            new_user = User(**user)
            new_user.save()


