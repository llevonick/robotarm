from django.conf.urls import  url

from . import views


urlpatterns= [
    url(r'^home/$', views.home, name='home'),
    url(r'^positions/$', views.display_positions, name='positions'),
    url(r'^raw_position/$', views.raw_positions, name='raw_position'),
    url(r'^set_servo$', views.set_position, name='set_servo'),
    url(r'^$', views.index, name='index'),
]
