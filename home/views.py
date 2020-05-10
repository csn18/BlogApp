from django.shortcuts import render
from django.views.generic import ListView

from st.models import *
from news.models import *


class MainNews(ListView):
    model = News
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(MainNews, self).get_context_data(**kwargs)
        ctx['news'] = News.objects.filter(on_main=True)
        ctx['st'] = Articles.objects.filter(on_main=True)
        ctx['main_news'] = News.objects.order_by('-id')[0:1]
        ctx['title'] = 'Главная'

        return ctx
