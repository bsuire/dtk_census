from django.conf.urls import url

from base_stats import views

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^data/(?P<variable>\w+)/$', views.stats, name='stats'),
    ]
