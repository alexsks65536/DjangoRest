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
        users = load_from_json("users")  # вызов ф-ии со значением имени файла user.json
        User.objects.all().delete()  # очистка значений в БД

        for user in users:
            new_user = User(**user)
            new_user.save()

        projects = load_from_json("projects")  # вызов ф-ии со значением
        Project.objects.all().delete()  # очистка значений в БД

        for project in projects:
            new_project = Project(**project)
            new_project.save()

        todos = load_from_json("todos")  # вызов ф-ии со значением
        Todo.objects.all().delete()  # очистка значений в БД

        for todo in todos:
            new_todo = Todo(**todo)
            new_todo.save()


