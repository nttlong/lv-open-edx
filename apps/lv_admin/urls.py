import quicky
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from . import views
import os
app=quicky.applications.get_app_by_file(__file__)
urlpatterns=[
    url(r'^$', views.index),
    url(r'^users$', views.index, name="users_admin"),
    app.get_static_urls(),
    url(r'^pages/(?P<path>.*)$', views.load_page, name='singleshop'),
    url(r'^api$',views.api),
    url(r'^login',views.login)
]
