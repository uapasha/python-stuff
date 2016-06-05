from django.conf.urls import patterns, url
from persons.views import (index, list_persons, manage_persons, register,
                           user_login, edit_person)

urlpatterns = [
    url(r'^$', index),

    url(r'^persons/$', list_persons),
    url(r'^manage/$', manage_persons),
    url(r'^modify_person/(?P<persons_short_name>[\w\W]+)/$', edit_person),
    url(r'^register/$', register),
    url(r'^login/$', user_login),
]
