'''
Created on Jul 15, 2013

@author: zero
'''
from django.conf.urls import patterns, url
from JSONService import views

urlpatterns = patterns('',
                       #/Mobile/
                       url(r'^$', views.index, name='index'),
                       #/Mobile/GetCountries/
                       url(r'^GetCountries/$', views.GetCountries, name='GetCountries'),
                       )