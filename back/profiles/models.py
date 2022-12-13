from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, blank=True, verbose_name='Фамилия')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(default='no bio...', max_length=300, verbose_name='Краткое описание')
    email = models.EmailField(max_length=200, blank=True, verbose_name='Email')
    country = models.CharField(max_length=200, blank=True, verbose_name='Страна')
    avatar = models.ImageField(upload_to='avatars/', default='avatar.png', verbose_name='Аватарка')
    friends = models.ManyToManyField(User, blank=True, related_name='friends', verbose_name='Друзья')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def get_friends(self):
        return self.friends.all()

    def get_friends_count(self):
        return self.friends.all().count()

    def get_post_count(self):
        return self.posts.all().count()

    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_count(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == 'Лайк':
                total_liked += 1
        return total_liked

    def get_likes_received_count(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked

    def __str__(self):
        return f"{self.user.username}–{self.created.strftime('%d-%m-%Y')}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


STATUS_CHOICES = (
    ('отправлено', 'отправлено'),
    ('приянто', 'приянто')
)


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver', verbose_name='Получатель')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, verbose_name='Статус')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'

    class Meta:
        verbose_name = 'Отношение'
        verbose_name_plural = 'Отношения'
