from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'create/$', views.GameCreateView.as_view(), name='game_create'),
    url(r'(?P<slug>.+)/$', views.GameDetailView.as_view(), name='game_detail'),
)