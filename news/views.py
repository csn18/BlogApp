from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpRequest, JsonResponse
from .models import *


class NewsView(ListView):
    paginate_by = 6
    model = News
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsView, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.order_by('-id')
        ctx['img_to_slider'] = News.objects.filter(img_to_slider=True)
        ctx['title'] = 'Новости'
        ctx['category'] = get_category()

        return ctx


def news(request):
    return JsonResponse({'hi': 'h1'})

class NewsTechnologies(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsTechnologies, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=1).order_by('-id')
        ctx['title'] = 'Технологии'
        ctx['category'] = get_category()

        return ctx


class NewsInternet(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsInternet, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=2).order_by('-id')
        ctx['title'] = 'Интернет'
        ctx['category'] = get_category()

        return ctx


class NewsRussia(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsRussia, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=3).order_by('-id')
        ctx['title'] = 'Россия'
        ctx['category'] = get_category()

        return ctx


class NewsUkraine(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsUkraine, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=4).order_by('-id')
        ctx['title'] = 'Украина'
        ctx['category'] = get_category()

        return ctx


class NewsSiriy(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsSiriy, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=5).order_by('-id')
        ctx['title'] = 'Сирия'
        ctx['category'] = get_category()

        return ctx


class NewsUSA(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsUSA, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=6)
        ctx['title'] = 'США'
        ctx['category'] = get_category()

        return ctx


class NewsPeople(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsPeople, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=7)
        ctx['title'] = 'Люди'
        ctx['category'] = get_category()

        return ctx


class NewsIT(ListView):
    model = News
    template_name = 'news/news_category.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsIT, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(category=8)
        ctx['title'] = 'IT'
        ctx['category'] = get_category()

        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        ctx['news'] = News.objects.order_by('-id')[0:4]

        return ctx


def get_category():
    category = CategoryNews.objects.all()
    all_category = dict()
    number = 0
    for item in category:
        number += 1
        all_category[item.name] = News.objects.filter(category=number).count()

    return all_category
