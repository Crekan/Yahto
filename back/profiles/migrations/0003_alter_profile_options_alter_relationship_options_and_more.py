# Generated by Django 4.1.4 on 2022-12-10 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_relationship'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterModelOptions(
            name='relationship',
            options={'verbose_name': 'Отношение', 'verbose_name_plural': 'Отношения'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to='avatars/', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='no bio...', max_length=300, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='Друзья'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обнавления'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='profiles.profile', verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='profiles.profile', verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('отправлено', 'отправлено'), ('приянто', 'приянто')], max_length=12, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обнавления'),
        ),
    ]
