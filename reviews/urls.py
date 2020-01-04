from django.conf.urls import url
from .views import all_reviews, review_detail, create_or_edit_review, upvotes

urlpatterns = [
    url(r'^$', all_reviews, name='get_reviews'),
    url(r'^(?P<pk>\d+)/$', review_detail, name='review_detail'),
    url(r'^new/$', create_or_edit_review, name='new_review'),
    url(r'^(?P<pk>\d+)/$', upvotes, name='upvotes'),
]