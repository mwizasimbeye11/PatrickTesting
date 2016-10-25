# -*- coding: utf-8 -*-

""" LimaProject URL Configuration """

from django.conf.urls import url, include
from django.contrib import admin
from Lima import views
from rest_framework.authtoken import views as authviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(views.api_v1.urls, namespace='api_v1')),
    url(r'^api/', authviews.obtain_auth_token),

]
