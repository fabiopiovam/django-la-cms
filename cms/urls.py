from django.conf.urls import url
from cms import views

app_name = 'cms'

urlpatterns = [
    url(r'^category/(?P<category_slug>.*?)/$', views.pages),
    url(r'^$', views.pages, name='pages'),
    url(r'^(?P<slug>.*?)/$', views.page, name='page'),
]
