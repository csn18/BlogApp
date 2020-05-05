from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='media/')
    author = models.CharField(max_length=128)
    publication_date = models.DateTimeField(auto_now_add=True)
    on_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
