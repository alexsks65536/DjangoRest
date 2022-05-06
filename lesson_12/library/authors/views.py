from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorSerializer, AuthorSerializerSuperUser, AuthorSerializerStaff


class AuthorModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListAPIView(ListAPIView):
    """Предоставляет метод get и выводит список данных из выборки queryset."""
    permission_classes = [AllowAny]
    # renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_serializer_class(self):
        if self.request.version == 'is_superuser':
            return AuthorSerializerSuperUser
        if self.request.version == 'is_staff':
            return AuthorSerializerStaff
        return AuthorSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    """Выдаёт метод get и выводит данные об одном объекте из выборки queryset.
    Для указания адреса требуется параметр pk, чтобы определить id элемента."""
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(UpdateAPIView):
    """Выдаёт методы put и patch для изменения объекта из выборки queryset.
    Требует pk в url-адресе. """
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class AuthorLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10
#
#
# class AuthorLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     pagination_class = AuthorLimitOffsetPagination
