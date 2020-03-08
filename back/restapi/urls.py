from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from restapi.views.alarm_clock_views import AlarmClockList, AlarmClockDetail
from restapi.views.backup_file_views import BackupFileView
from restapi.views.player_views import PlayerStatus
from restapi.views.system_date_view import SystemDateView
from restapi.views.volume_views import VolumeView
from restapi.views.web_radio_views import WebRadioList, WebRadioDetail

router = DefaultRouter(trailing_slash=False)


web_radio_urlpatterns = [
    url(r'^$', WebRadioList.as_view(), name="list_create"),
    url(r'^(?P<pk>[0-9]+)/$', WebRadioDetail.as_view(), name="retrieve_update_destroy"),
]

alarm_clock_urlpatterns = [
    url(r'^$', AlarmClockList.as_view(), name="list_create"),
    url(r'^(?P<pk>[0-9]+)/$', AlarmClockDetail.as_view(), name="retrieve_update_destroy"),
]

player_urlpatterns = [
    url(r'^$', PlayerStatus.as_view(), name="get_player_or_update"),
]

clock_urlpatterns = [
    url(r'^$', SystemDateView.as_view(), name="get_clock"),
]

volume_urlpatterns = [
    url(r'^$', VolumeView.as_view(), name="get_or_update_volume"),
]

backup_urlpatterns = [
    url(r'^$', BackupFileView.as_view(), name="list_create"),
]


urlpatterns = [
    url(r'^webradios/', include((web_radio_urlpatterns, 'webradios'), namespace='webradios')),
    url(r'^alarmclocks/', include((alarm_clock_urlpatterns, 'alarmclocks'), namespace='alarmclocks')),
    url(r'^player/', include((player_urlpatterns, 'player'), namespace='player')),
    url(r'^clock/', include((clock_urlpatterns, 'clock'), namespace='clock')),
    url(r'^volume/', include((volume_urlpatterns, 'volume'), namespace='volume')),
    url(r'^backup/', include((backup_urlpatterns, 'backup'), namespace='backup'))
]
