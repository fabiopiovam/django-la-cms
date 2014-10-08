from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms.views',
    url(r'^category/(?P<category_slug>.*?)/$', 'pages'),
    url(r'^$', 'pages', name='pages'),
    url(r'^(?P<slug>.*?)/$', 'page', name='page'),
)