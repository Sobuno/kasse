"""kasse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from __future__ import absolute_import, unicode_literals, division

from django.conf.urls import include, url
from django.contrib import admin

from kasse.views import (
    Home, Log, Login, Logout, ProfileCreate, ChangePassword, ProfileView,
    ProfileEdit, ProfileEditAdmin, UserCreate, Association, ProfileList,
    ProfileMerge,
)
import stopwatch.urls
import iou.urls
import news.urls
from stopwatch.views import TimeTrialStopwatchOffline

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timetrial/', include(stopwatch.urls)),
    url(r'^news/', include(news.urls)),
    url(r'^iou/', include(iou.urls)),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^log/$', Log.as_view(), name='log'),

    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^password/$', ChangePassword.as_view(), name='password'),

    url(r'^newuser/$', UserCreate.as_view(),
        name='newuserprofile'),
    url(r'^newuser/(?P<pk>\d+)/$', UserCreate.as_view(),
        name='newuser'),
    url(r'^profile/$', ProfileList.as_view(),
        name='profile_list'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(),
        name='profile'),
    url(r'^profile/(?P<pk>\d+)/merge/$', ProfileMerge.as_view(),
        name='profile_merge'),
    url(r'^profile/edit/$', ProfileEdit.as_view(),
        name='profile_edit'),
    url(r'^profile/edit/(?P<pk>\d+)/$', ProfileEditAdmin.as_view(),
        name='profile_edit_admin'),
    url(r'^profile/create/$', ProfileCreate.as_view(),
        name='profile_create'),
    url(r'^stopwatch/$', TimeTrialStopwatchOffline.as_view(),
        name='timetrial_stopwatch_offline'),

    url(r'^association/$', Association.as_view(),
        name='association'),
]
