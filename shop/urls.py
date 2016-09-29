from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='shop.index'),
    url(r'^list$', views.list, name='shop.list'),
    url(r'^item/(\d+)$', views.item, name='shop.item'),
    url(r'^add$', views.add, name='shop.add'),
    url(r'^delete$', views.delete, name='shop.delete'),
    url(r'^update$', views.update, name='shop.update'),
    url(r'^cart$', views.cart, name='shop.cart'),
]

