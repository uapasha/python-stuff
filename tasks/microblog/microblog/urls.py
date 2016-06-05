from django.conf import settings
from django.conf.urls import patterns, include, url
# enable the admin:
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomepageView.as_view(), name = 'home'),
    url(r'^blog/', include('blog.urls', namespace = 'blog')), 

    #  enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', 
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document.root': settings.STATIC_ROOT}),
    )