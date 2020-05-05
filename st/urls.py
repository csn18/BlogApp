from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllArticlesView.as_view(), name='st-home'),
    path('<int:pk>', views.ArticlesDetailView.as_view(), name='st-detail'),
]
