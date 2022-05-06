from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from authors.models import Author


# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializerSuperUser(ModelSerializer):
    class Meta:
        model = Author
        fields = ('username', 'firstname', 'lastname', 'email')


class AuthorSerializerStaff(ModelSerializer):
    class Meta:
        model = Author
        fields = ('username', 'email')
