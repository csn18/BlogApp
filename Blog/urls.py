from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('st/', include('st.urls')),
    path('news/', include('news.urls')),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
