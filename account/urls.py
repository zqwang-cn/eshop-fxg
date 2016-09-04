from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin$', views.signin, name='account.signin'),
    url(r'^signup$', views.signup, name='account.signup'),
    url(r'^signout$', views.signout, name='account.signout'),
    url(r'^detail$', views.detail, name='account.detail'),
    url(r'^sendcode$', views.sendcode, name='account.sendcode'),
]

