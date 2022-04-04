# Generated by Django 4.0.3 on 2022-03-09 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('repository', models.CharField(max_length=250)),
                ('user', models.ManyToManyField(to='users.user')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2022-03-09')),
                ('isactive', models.BooleanField(default=True)),
                ('project', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
