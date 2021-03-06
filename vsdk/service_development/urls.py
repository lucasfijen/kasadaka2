from django.conf.urls import url, include

from . import views

app_name= 'service-development'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^choice/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.choice, name='choice'),
    url(r'^message/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.message_presentation, name='message-presentation'),
    url(r'^start/(?P<voice_service_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^start/(?P<voice_service_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^user/register/(?P<session_id>[0-9]+)$', views.KasaDakaUserRegistration.as_view(), name = 'user-registration'),
    url(r'^language_select/(?P<session_id>[0-9]+)$', views.LanguageSelection.as_view(), name = 'language-selection'),
    url(r'^record/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.record, name='record'),
    url(r'^offers/(?P<session_id>[0-9]+)$', views.offer, name='offers'),
    url(r'^show_offer/(?P<session_id>[0-9]+)/(?P<offer_id>[0-9]+)$', views.show_offer, name='show_offer'),
    url(r'^region/(?P<session_id>[0-9]+)$', views.RegionSelection.as_view(), name='region'),
    url(r'^product/(?P<session_id>[0-9]+)$', views.ProductSelection.as_view(), name='product'),
    url(r'^lendrent/(?P<session_id>[0-9]+)$', views.LendRentSelection.as_view(), name='lendrent'),
    url(r'^lendorrentredirect/(?P<session_id>[0-9]+)$', views.lendrentredirect, name='lendorrentredirect'),
    url(r'^offerplacing/(?P<session_id>[0-9]+)$', views.offerplacing, name='offerplacing'),
]

