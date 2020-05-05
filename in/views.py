from django.shortcuts import render


def interview(requests):
    title = 'Интервью'
    return render(requests, 'in/interview.html', locals())
