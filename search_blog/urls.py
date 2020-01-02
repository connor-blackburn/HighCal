from django.conf.urls import url
from .views import do_search_blog

urlpatterns = [
    url(r'^$', do_search_blog, name='search_blog')
] 