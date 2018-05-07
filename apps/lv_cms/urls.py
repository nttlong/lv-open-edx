import quicky
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
import os
app=quicky.applications.get_app_by_file(__file__)
urlpatterns=[
    app.get_static_urls(),
]
