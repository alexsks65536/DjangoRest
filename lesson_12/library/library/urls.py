"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from todolist.views import ProjectModelViewSet, TodoModelViewSet, ProjectListAPIView, ProjectRetrieveAPIView, \
    ProjectCreateAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, TodoListAPIView, TodoRetrieveAPIView, \
    TodoCreateAPIView, TodoUpdateAPIView, TodoDestroyAPIView, ProjectCustomDjangoFilterViewSet
# from todolist.views import ProjectModelViewSet, TodoModelViewSet
from authors.views import AuthorListAPIView, AuthorUpdateAPIView, AuthorModelViewSet, AuthorRetrieveAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from graphene_django.views import GraphQLView


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todolist', TodoModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/author/', AuthorListAPIView.as_view()),
    path('api/author/<int:pk>/', AuthorRetrieveAPIView.as_view()),
    path('api/author/update/<int:pk>/', AuthorUpdateAPIView.as_view()),
    path('project/', include(router.urls)),
    path('api/project/list/', ProjectListAPIView.as_view()),
    path('api/project/retrieve/<int:pk>/', ProjectRetrieveAPIView.as_view()),
    path('api/project/create/', ProjectCreateAPIView.as_view()),
    path('api/project/update/<int:pk>/', ProjectUpdateAPIView.as_view()),
    path('api/project/destroy/<int:pk>/', ProjectDestroyAPIView.as_view()),
    path('api/todo/list/', TodoListAPIView.as_view()),
    path('api/todo/retrieve/<int:pk>/', TodoRetrieveAPIView.as_view()),
    path('api/todo/create/', TodoCreateAPIView.as_view()),
    path('api/todo/update/<int:pk>/', TodoUpdateAPIView.as_view()),
    path('api/todo/destroy/<int:pk>/', TodoDestroyAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    # path('api/project/filters/<str:title>/', ProjectCustomDjangoFilterViewSet.as_view()),
    path('api/<version>/authors/', AuthorListAPIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]
