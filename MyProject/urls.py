from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from MyApp.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
