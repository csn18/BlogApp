from django.contrib.auth.models import User
from django.db import models
from news.models import News


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/image_user/noimage.png', upload_to='media/image_user')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

