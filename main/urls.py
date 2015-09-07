from django.conf.urls import patterns, url, include

urlpatterns = patterns('main.views',

   url(r'^home$', 'home'),
)
