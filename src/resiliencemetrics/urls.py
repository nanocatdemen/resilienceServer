from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^viz$', views.viz_metrics, name='viz_metrics'),
    url(r'^metrics/(?P<id>\w{0,50})$', views.show_metric, name='show_metric'),
    url(r'^metrics$', views.list_metrics, name='list_metrics'),
    url(r'^papers/(?P<id>\w{0,50})$', views.show_paper, name='show_paper'),
    url(r'^papers$', views.list_papers, name='list_papers'),
    url(r'^$', views.home, name='home')
]
