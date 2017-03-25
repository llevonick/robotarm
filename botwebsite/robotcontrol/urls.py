from django.conf.urls import  url

from . import views


urlpatterns= [
    url(r'^home/$', views.home, name='home'),
    url(r'^positions/$', views.display_positions, name='positions'),
    url(r'^$', views.index, name='index'),
]
