from django.conf.urls import patterns, url

from selamlama import views

urlpatterns=patterns('',
	url(r'^$', views.hello_world, name='helloworld')
)
