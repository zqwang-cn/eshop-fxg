from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='shop.index'),
    url(r'^all$', views.all, name='shop.all'),
    url(r'^item/(\d+)$', views.item, name='shop.item'),
]

