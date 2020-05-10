from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainNews.as_view(), name='home-home')
]
