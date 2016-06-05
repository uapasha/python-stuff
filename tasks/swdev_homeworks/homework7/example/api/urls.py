from django.conf.urls import url
from api.views import persons_json_list, add_person, delete_person

urlpatterns = [
    url(r'^list_persons$', persons_json_list),
    url(r'^add_person$', add_person),
    url(r'^delete_persons/(?P<substr>[\w\W]+)/$', delete_person),
    ]