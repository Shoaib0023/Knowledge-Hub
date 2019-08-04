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

# if settings.DEBUG:
#      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
