from django.conf.urls import url
# from . import views

from .views import (
    home,
    list_papers,
    list_metrics,
    paper_detail,
    metric_detail,
    viz_metrics,
    )

urlpatterns = [
    url(r'^$', home),
    url(r'^metrics/(?P<id>\d+)/$', metric_detail, name='metric_detail'),
    url(r'^metrics/$', list_metrics),
    url(r'^papers/(?P<id>\d+)/$', paper_detail, name='paper_detail'),
    url(r'^papers/$', list_papers),
    url(r'^viz/$', viz_metrics),
]
