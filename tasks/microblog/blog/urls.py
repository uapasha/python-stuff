from django.conf.urls import patterns, url
# enable the admin:

from . import views


urlpatterns = patterns('',
    url(r'^comments/$', views.comments_all, name = 'comments'),
    url(r'^$', views.PostListView.as_view(), name = 'list'), 
    url(r'^(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name = 'detail'),
    url(r'^add_comment$', views.add_comment, name = 'add_comment')
    
)
