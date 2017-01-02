"""piclodio3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from webapi.views import BackupFileView
from webapi.views import PlayerView
from webapi.views import WebRadioView
from webapi.views import AlarmClockView
from webapi.views import SystemDateView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # used by Django rest framework for dev
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # piclodio URLs
    url(r'^webradio/?$', WebRadioView.WebRadioList.as_view()),
    url(r'^webradio/(?P<pk>[0-9]+)/?$', WebRadioView.WebRadioDetail.as_view()),

    url(r'^alarms/$', AlarmClockView.AlarmClockList.as_view()),
    url(r'^alarms/(?P<pk>[0-9]+)/?$', AlarmClockView.AlarmClockDetail.as_view()),

    url(r'^systemdate/?$', SystemDateView.SystemDateList.as_view()),
    url(r'^player/?$', PlayerView.PlayerStatus.as_view()),

    url(r'^backup/?$', BackupFileView.BackupFileView.as_view()),

]
