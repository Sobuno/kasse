"""kasse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from __future__ import absolute_import, unicode_literals, division

from django.conf.urls import include, url
from django.contrib import admin

from kasse.views import (
    Home, Login, Logout,
    TimeTrialCreate, TimeTrialDetail, TimeTrialList
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', Home.as_view(), name='home'),

    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),

    url(r'^timetrial/$', TimeTrialList.as_view(),
        name='timetrial_list'),
    url(r'^timetrial/create/$', TimeTrialCreate.as_view(),
        name='timetrial_create'),
    url(r'^timetrial/(?P<pk>\d+)/$', TimeTrialDetail.as_view(),
        name='timetrial_detail'),
]
