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
    app.get_static_urls()
]
            # + static("^static\/(?P<path>.*)$", document_root="/home/hcsadmin/edx-ginkgo.2-3/apps/edx/edx-platform/lv-packages/lv_admin/static")