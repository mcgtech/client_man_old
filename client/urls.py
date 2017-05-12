from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^client_list$', views.client_list, name='client_list'),
    url(r'^client/new/$', views.client_new, name='client_new'),
]