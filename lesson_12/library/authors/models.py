from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField('email address', blank=True, unique=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
