from django.conf.urls import patterns, url

from chvote import views


urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
    	#url(r'^reservation$', views.reservation, name='reservation')
)