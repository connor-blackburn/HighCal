from django.conf.urls import url, include
from .views import all_portfolio

urlpatterns = [
    url(r'^$', all_portfolio, name='portfolios'),
] 