from django.shortcuts import render


def home(requests):
    title = 'Главная'
    return render(requests, 'home/home.html', locals())
