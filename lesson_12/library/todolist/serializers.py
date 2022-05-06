from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Project, Todo
from authors.serializers import AuthorSerializer


# class ProjectSerializer(serializers.HyperlinkedModelSerializer):
#     author = AuthorSerializer(many=True)
#
#     class Meta:
#         model = Project
#         fields = '__all__'


class ProjectSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Project
        fields = '__all__'


# class TodoSerializer(serializers.HyperlinkedModelSerializer):
#     author = AuthorSerializer()
#
#     class Meta:
#         model = Todo
#         fields = '__all__'

class TodoSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
