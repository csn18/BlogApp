from django.db import models
from django.urls import reverse


class CategoryNews(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='media/news')
    author = models.CharField(max_length=128)
    category = models.ForeignKey(CategoryNews, blank=True, null=True, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    on_main = models.BooleanField(default=False)
    img_to_slider = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
