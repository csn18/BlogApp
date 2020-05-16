from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from user.forms import UserCreate
from django.contrib.auth.decorators import login_required


def register(request):
    if request.POST:
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreate()
    return render(request, 'user/register.html', locals())


@login_required
def profile(request):
    return render(request, 'user/profile.html')
