from django.conf.urls import url
from hello_world_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^home/$', views.home, name='home'),

]