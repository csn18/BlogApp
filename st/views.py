from django.shortcuts import render
from django.views.generic import (ListView, DetailView)

from news.models import *
from .models import *


class AllArticlesView(ListView):
    model = Articles
    template_name = 'st/articles.html'

    def get_context_data(self, **kwargs):
        ctx = super(AllArticlesView, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.order_by('-id')
        ctx['img_to_slider'] = Articles.objects.filter(img_to_slider=True)
        ctx['title'] = 'Статьи'
        ctx['category'] = get_category()

        return ctx


class ArticlesProgramming(ListView):
    model = Articles
    template_name = 'st/articles_programming.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesProgramming, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.filter(category=1).order_by('-id')
        ctx['title'] = 'Программирование'
        ctx['category'] = get_category()

        return ctx


class ArticlesNewTecnologies(ListView):
    model = Articles
    template_name = 'st/articles_new_tecnologies.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesNewTecnologies, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.filter(category=2).order_by('-id')
        ctx['title'] = 'Новые технологии'
        ctx['category'] = get_category()

        return ctx


class ArticlesIT(ListView):
    model = Articles
    template_name = 'st/articles_it.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesIT, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.filter(category=3).order_by('-id')
        ctx['title'] = 'IT'
        ctx['category'] = get_category()

        return ctx


class ArticlesOS(ListView):
    model = Articles
    template_name = 'st/articles_os.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesOS, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.filter(category=4).order_by('-id')
        ctx['title'] = 'OS'
        ctx['category'] = get_category()

        return ctx


class ArticlesMacIOS(ListView):
    model = Articles
    template_name = 'st/articles_mac_ios.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesMacIOS, self).get_context_data(**kwargs)
        ctx['posts'] = Articles.objects.filter(category=5).order_by('-id')
        ctx['title'] = 'Mac iOS'
        ctx['category'] = get_category()

        return ctx


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'st/articles_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesDetailView, self).get_context_data(**kwargs)
        ctx['title'] = Articles.objects.filter(pk=self.kwargs['pk']).first()
        ctx['news'] = News.objects.order_by('-id')[0:4]

        return ctx


def get_category():
    category = CategoryArticles.objects.all()
    all_category = dict()
    number = 0
    for item in category:
        number += 1
        all_category[item.name] = Articles.objects.filter(category=number).count()

    return all_category
