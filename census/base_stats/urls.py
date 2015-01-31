from django.conf.urls import url

from base_stats import views

urlpatterns = [
        url(r'^$', views.stats, name='stats'),
    ]
