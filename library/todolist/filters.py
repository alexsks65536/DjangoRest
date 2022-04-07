# from rest_framework import viewsets
# from rest_framework.generics import ListAPIView
#
# from todolist.models import Project, Todo
# from todolist.serializers import ProjectSerializer, TodoSerializer
#

# class ProjectDjangoFilterViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     filterset_fields = ['name', 'repository', 'user']
#
#
# class TodoKwargsFilterView(ListAPIView):
#     serializer_class = TodoSerializer
#
#     def get_queryset(self):
#         title = self.kwargs['title']
#         return Todo.objects.filter(title__contains=title)

from django_filters import rest_framework as filters
from .models import Project


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']
