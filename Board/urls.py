from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from WebBoard import urls
from Search import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('Search.urls', namespace='search')),
    path('', include('WebBoard.urls')),
]
