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
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from todolist.views import ProjectModelViewSet, TodoModelViewSet, ProjectListAPIView, ProjectRetrieveAPIView, \
    ProjectCreateAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, TodoListAPIView, TodoRetrieveAPIView, \
    TodoCreateAPIView, TodoUpdateAPIView, TodoDestroyAPIView, ProjectCustomDjangoFilterViewSet
# from todolist.views import ProjectModelViewSet, TodoModelViewSet
from users.views import UserListAPIView, UserUpdateAPIView, UserModelViewSet, UserRetrieveAPIView

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todolist', TodoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/user/', UserListAPIView.as_view()),
    path('api/user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('api/user/update/<int:pk>/', UserUpdateAPIView.as_view()),
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
    path('api-token-auth/', views.obtain_auth_token)
    # path('api/project/filters/<str:title>/', ProjectCustomDjangoFilterViewSet.as_view())
]
