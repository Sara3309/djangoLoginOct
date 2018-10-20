from django.conf.urls import url
from . import views
urlpatterns= [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    # url(r'success$',views.success),
    url(r'back$', views.back),
    url(r'wall$', views.wall),
    url(r'post_message', views.post_message),
    url(r'(?P<id>\d+)/delete_message$',views.delete_message),
    url(r'(?P<id>\d+)/delete_comment$',views.delete_comment),
    url(r'(?P<id>\d+)/post_comment$', views.post_comment)
]