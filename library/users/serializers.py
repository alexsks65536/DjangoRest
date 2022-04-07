from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerSuperuser(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email')


class UserSerializerStaff(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
