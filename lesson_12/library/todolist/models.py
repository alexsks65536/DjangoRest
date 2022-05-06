from django.db import models
from django.utils import timezone
from authors.models import Author


class Project(models.Model):
    """Проект"""
    name = models.CharField(max_length=100)  # название Проекта
    repository = models.CharField(max_length=250)  # ссылка на репозиторий
    author = models.ForeignKey(Author, models.PROTECT)

    class Meta:
        verbose_name = ('Project')  # имя Проекта
        verbose_name_plural = ('Projects')  # множественное имя для Проекта

    def __str__(self):
        return self.name


class Todo(models.Model):
    """Заметка"""
    title = models.CharField(max_length=250)  # название Заметки
    content = models.TextField(blank=True)  # текстовое поле Заметки
    author = models.ForeignKey(Author, models.PROTECT)
    created = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))  # дата создания Заметки
    project = models.ForeignKey(Project, default='general', on_delete=models.PROTECT)  # foreignkey с помощью которой мы будем осуществлять связь
    isactive = models.BooleanField(default=True)  # признак активности Заметки

    class Meta:  # вспомогательный класс для сортировки
        ordering = ['-created']  # сортировка Заметок по времени их создания

    def __str__(self):
        return self.title
