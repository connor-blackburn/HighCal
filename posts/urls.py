from django.conf.urls import url
from .views import get_posts, post_detail

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail')
] 