from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView.as_view(), name='news-home'),
    path('technologies', views.NewsTechnologies.as_view(), name='news-technologies'),
    path('internet', views.NewsInternet.as_view(), name='news-internet'),
    path('russia', views.NewsRussia.as_view(), name='news-russia'),
    path('ukraine', views.NewsUkraine.as_view(), name='news-ukraine'),
    path('siriy', views.NewsSiriy.as_view(), name='news-siriy'),
    path('usa', views.NewsUSA.as_view(), name='news-usa'),
    path('people', views.NewsPeople.as_view(), name='news-people'),
    path('it', views.NewsIT.as_view(), name='news-it'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]
