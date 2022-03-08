from rest_framework import serializers
from .models import Project, Todo
from users.serializers import UserSerializer


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
