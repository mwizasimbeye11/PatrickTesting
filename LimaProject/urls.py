# -*- coding: utf-8 -*-

""" LimaProject URL Configuration """

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views as v
from Lima import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(views.api_v1.urls, namespace='api_v1')),
    #url(r'^token/', v.obtain_auth_token),
]
