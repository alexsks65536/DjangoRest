from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todolist.models import Project, Todo
from authors.models import Author


class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.all().delete()
        # Project.objects.all().delete()
        # T odo.objects.all().delete()
        # Author.objects.all().delete()

        User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        User.objects.create_superuser('admin', 'admin@geekshop.local', 'geekbrains')
        User.objects.create_user('user', 'user@geekshop.local', 'geekbrains')

        projects = [
            {
                "name": "DJANGO REST FRAMEWORK",
                "repository": "https://github.com/tomchristie/django-rest-framework",
                "author_id": 1
            },
            {
                "name": "DJANGO-REST-FRAMEWORK-SIMPLEJWT",
                "repository": "https://github.com/jazzband/djangorestframework-simplejwt",
                "author_id": 1
            },
            {
                "name": "DRF-YASG",
                "repository": "https://github.com/axnsan12/drf-yasg",
                "author_id": 1
            },
            {
                "name": "DJOSER",
                "repository": "https://github.com/sunscrapers/djoser",
                "author_id": 1
            },
            {
                "name": "DJANGO OAUTH TOOLKIT",
                "repository": "https://github.com/evonove/django-oauth-toolkit",
                "author_id": 1
            },
            {
                "name": "DRF-EXTENSIONS",
                "repository": "https://github.com/chibisov/drf-extensions",
                "author_id": 1
            },
            {
                "name": "COOKIECUTTER-DJANGO-REST",
                "repository": "https://github.com/agconti/cookiecutter-django-rest",
                "author_id": 1
            },
            {
                "name": "DJANGO REST FRAMEWORK JSON API",
                "repository": "https://github.com/django-json-api/django-rest-framework-json-api",
                "author_id": 1
            },
            {
                "name": "DJANGO-REST-KNOX",
                "repository": "https://github.com/James1345/django-rest-knox",
                "author_id": 1
            },
            {
                "name": "DJANGO-REST-FRAMEWORK-GIS",
                "repository": "https://github.com/djangonauts/django-rest-framework-gis",
                "author_id": 1
            }
        ]

        todos = [
            {"title": "Aenean sit amet justo.",
             "content": "Sed ante. Vivamus tortor. Duis mattis egestas metus.\n\nAenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.\n\nQuisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.\n\nVestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.",
             "created": "2021-09-08", "author_id": 1, "project_id": 1},
            {"title": "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
             "content": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.\n\nPellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.\n\nCum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nEtiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.\n\nPraesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.\n\nCras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
             "created": "2021-06-19", "author_id": 1, "project_id": 1},
            {"title": "Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.",
             "content": "Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.\n\nPhasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.\n\nProin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.\n\nDuis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.",
             "created": "2021-05-27", "author_id": 1, "project_id": 1},
            {"title": "Proin at turpis a pede posuere nonummy.",
             "content": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.\n\nCurabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.\n\nPhasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.\n\nProin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.",
             "created": "2021-10-23", "author_id": 1, "project_id": 1},
            {"title": "Vestibulum ac est lacinia nisi venenatis tristique.",
             "content": "Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.\n\nMauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.\n\nNullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.\n\nIn quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.\n\nMaecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.",
             "created": "2022-01-18", "author_id": 1, "project_id": 1},
            {"title": "Etiam justo.",
             "content": "Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.\n\nQuisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.\n\nVestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.\n\nIn congue. Etiam justo. Etiam pretium iaculis justo.\n\nIn hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.\n\nNulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.\n\nCras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.\n\nQuisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.\n\nPhasellus in felis. Donec semper sapien a libero. Nam dui.",
             "created": "2021-11-14", "author_id": 1, "project_id": 1},
            {"title": "Donec quis orci eget orci vehicula condimentum.",
             "content": "Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.\n\nDonec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.\n\nIn sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.\n\nSuspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.\n\nCurabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.\n\nInteger tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.\n\nPraesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
             "created": "2021-06-16", "author_id": 1, "project_id": 1},
            {"title": "Integer non velit.",
             "content": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.\n\nMorbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.\n\nFusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.\n\nSed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.\n\nPellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.\n\nCum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n\nEtiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.\n\nPraesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.\n\nCras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
             "created": "2021-05-26", "author_id": 1, "project_id": 1},
            {"title": "Integer tincidunt ante vel ipsum.",
             "content": "Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.\n\nPhasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.\n\nProin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.\n\nDuis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.\n\nDonec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.\n\nIn sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.\n\nSuspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.\n\nCurabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.",
             "created": "2021-08-07", "author_id": 1, "project_id": 1},
            {"title": "Integer non velit.",
             "content": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.\n\nProin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.\n\nDuis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.\n\nDonec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.\n\nIn sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.",
             "created": "2021-10-09", "author_id": 1, "project_id": 1}
        ]

        authors = [
            {
                "username": "JohnsLord",
                "firstname": "John",
                "lastname": "Lords",
                "email": "johnslord@geek.brains"
            },
            {
                "username": "TomCruise",
                "firstname": "Tom",
                "lastname": "Cruise",
                "email": "tomcruise@geek.brains"
            },
            {
                "username": "DmitryMedvedev",
                "firstname": "Dmitry",
                "lastname": "Medvedev",
                "email": "dmitrymedvedev@geek.brains"
            },
            {
                "username": "GarryMoore",
                "firstname": "Garry",
                "lastname": "Moore",
                "email": "afterthewar@geek.brains"
            },
            {
                "username": "PoleStanley",
                "firstname": "Pole",
                "lastname": "Stanly",
                "email": "kisskiss@geek.brains"
            }
        ]

        # for item in authors:
        #     Author.objects.create(**item)

        for item in projects:
            Project.objects.create(**item)

        for item in todos:
            Todo.objects.create(**item)
