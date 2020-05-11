from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AllArticlesView.as_view(), name='st-home'),
    path('programming', views.ArticlesProgramming.as_view(), name='articles-programming'),
    path('new_technologies', views.ArticlesNewTechnologies.as_view(), name='articles-new_technologies'),
    path('it', views.ArticlesIT.as_view(), name='articles-it'),
    path('os', views.ArticlesOS.as_view(), name='articles-os'),
    path('mac_ios', views.ArticlesMacIOS.as_view(), name='articles-mac_ios'),
    path('<int:pk>', views.ArticlesDetailView.as_view(), name='st-detail'),
]
