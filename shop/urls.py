from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='shop.index'),
    url(r'^list$', views.list, name='shop.list'),
    url(r'^item/(\d+)$', views.item, name='shop.item'),
]

