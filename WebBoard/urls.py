from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'', views.home, name="home"),
    # accounts related urls
    url(r'^home/signup/$', views.signup, name="signup"),
    url(r'^accounts/login/$', login, {'template_name':'accounts/login.html'}, name="login"),
    url(r'^accounts/logout/$', logout, name="logout"),
    # app functionality related urls
    url(r'^home/myposts/$', views.my_post, name="mypost"),
    url(r'^home/questions/$', views.all_posts, name="allposts"),
    url(r'^home/questions/mostviewed/$', views.most_viewed_post, name="mostviewed"),
    url(r'^home/questions/(?P<pk>\d+)/like/$', views.likefunc, name="likefunc"),
    url(r'^home/questions/ask/$', views.ask_question, name="askquestion"),
    url(r'^home/questions/(?P<pk>\d+)/reply/$', views.reply_post, name="replypost"),
    url(r'^home/questions/(?P<pk>\d+)/edit/$', views.edit_post, name="editpost"),
    url(r'^home/questions/(?P<pk>\d+)/$', views.post, name="post"),
    url(r'^home/topic/(?P<pk>\d+)/$', views.topicpostview, name="topicpostview"),
    # user profile urls
    url(r'^home/(?P<pk>\d+)/profile/$', views.profile, name="profile"),
    url(r'^home/(?P<pk>\d+)/profile/edit/$', views.edit_profile, name="editprofile"),
]
