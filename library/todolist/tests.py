import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet
from .models import Project, Todo


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'name': 'Project-Umbrella', 'repository': 'https://umbrella.com'}, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'name': 'Project-Umbrella', 'repository': 'https://umbrella.com'}, format='json')
        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        project = Project.objects.create(name='DJANGO-REST-FRAMEWORK-SIMPLEJWT', repository='https://github.com/jazzband/djangorestframework-simplejwt')
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        todo = Project.objects.create(name='Project-Philadelphia', birthday_year='https://ru.wikipedia.org/wiki')
        client = APIClient()
        response = client.put(f'/api/todolist/{todo.id}/', {'title': 'TestTodo', 'content': 'someContent'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        project = Project.objects.create(name='projectProject', repository='123123123')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/projects/{project.id}/', {'name': 'DJANGO-REST-FRAMEWORK-SIMPLEJWT', 'repository': 'https://github.com/jazzband/djangorestframework-simplejwt'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'Грин')
        self.assertEqual(project.repository, 'https://git-repo.com')
        client.logout()

    

















