from rest_framework import viewsets, filters, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from .filters import ProjectFilter
from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'repository', 'user']


class ProjectListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class ProjectAPIView(viewsets.ViewSet):
#
#     def list(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects)
#         return Response(serializer.data)

"""Это не заработало("""
# class ProjectModelViewSet(
#                             mixins.ListModelMixin,
#                             mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             viewsets.GenericViewSet
#                         ):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


class ProjectCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    
class TodoListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    
# class TodoLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#
#
# class TodoLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     pagination_class = TodoLimitOffsetPagination

