from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^papers$', views.list_papers, name='list_papers'),
    url(r'^$', views.home, name='home')
]
