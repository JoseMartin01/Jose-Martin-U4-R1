from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hello_world, name='hello'),
    url(r'^(?P<pk>[0-9]+)/$', views.product_detail, name="detail"),
    url(r'^new', views.new_product, name="new_product")
]

