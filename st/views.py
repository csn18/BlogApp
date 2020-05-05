from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import *


class AllArticlesView(ListView):
    model = Articles
    context_object_name = 'posts'
    template_name = 'st/articles.html'

    def get_context_data(self, **kwargs):
        ctx = super(AllArticlesView, self).get_context_data(**kwargs)
        ctx['title'] = 'Статьи'

        return ctx


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'st/articles_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticlesDetailView, self).get_context_data(**kwargs)
        ctx['title'] = Articles.objects.filter(pk=self.kwargs['pk']).first()
        ctx['posts'] = Articles.objects.order_by('-id')[0:3]

        return ctx
