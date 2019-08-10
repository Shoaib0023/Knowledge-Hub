from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    # accounts related urls
    url(r'^accounts/signup/$', views.signup, name="signup"),
    url(r'^accounts/login/$', login, {'template_name':'accounts/login.html'}, name="login"),
    # url(r'^accounts/logout/$', views.auth_logout, name="logout"),
    # url(r'accounts/login/$', views.auth_login, name="login"),
    url(r'accounts/logout', logout, name="logout"),

    # app functionality related urls
    url(r'^myposts/$', views.my_post, name="mypost"),
    url(r'^questions/$', views.all_posts, name="allposts"),
    url(r'^questions/mostviewed/$', views.most_viewed_post, name="mostviewed"),
    url(r'^questions/(?P<pk>\d+)/like/$', views.likefunc, name="likefunc"),
    url(r'^questions/ask/$', views.ask_question, name="askquestion"),
    url(r'^questions/(?P<pk>\d+)/reply/$', views.reply_post, name="replypost"),
    url(r'^questions/(?P<pk>\d+)/edit/$', views.edit_post, name="editpost"),
    url(r'^questions/(?P<pk>\d+)/$', views.post, name="post"),
    url(r'^topic/(?P<pk>\d+)/$', views.topicpostview, name="topicpostview"),

    url(r'^(?P<pk>\d+)/profile/$', views.profile, name="profile"),
    url(r'^(?P<pk>\d+)/profile/edit/$', views.edit_profile, name="editprofile"),
    url(r'', views.home, name="home"),
]
