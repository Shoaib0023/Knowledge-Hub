app_name = "search"

from django.conf.urls import url
from . import views as SearchView

urlpatterns =  [
    url(r'^$', SearchView.search, name="query")
]
