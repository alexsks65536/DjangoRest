from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """Предоставляет метод get и выводит список данных из выборки queryset."""
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """Выдаёт метод get и выводит данные об одном объекте из выборки queryset.
    Для указания адреса требуется параметр pk, чтобы определить id элемента."""
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Выдаёт методы put и patch для изменения объекта из выборки queryset.
    Требует pk в url-адресе. """
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10
#
#
# class UserLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     pagination_class = UserLimitOffsetPagination
