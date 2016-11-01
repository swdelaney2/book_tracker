from django.conf.urls import url

from . import views

app_name = 'tracker'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^(?P<book_id>[0-9]+)/change_read_status/(?P<status>[\w-]+)/$', views.change_read_status, name='change_read_status'),
    url(r'^listing/$', views.listing, name='listing'),

]
