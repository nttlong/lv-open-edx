"""
URLs for LMS
"""

from config_models.views import ConfigurationModelCurrentAPIView
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from ratelimitbackend import admin

from courseware.views.index import CoursewareIndex
from courseware.views.views import CourseTabView, EnrollStaffView, StaticCourseTabView
from django_comment_common.models import ForumsConfig
from openedx.core.djangoapps.auth_exchange.views import LoginWithAccessTokenView
from openedx.core.djangoapps.catalog.models import CatalogIntegration
from openedx.core.djangoapps.programs.models import ProgramsApiConfig
from openedx.core.djangoapps.self_paced.models import SelfPacedConfiguration
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.features.enterprise_support.api import enterprise_enabled


# Uncomment the next two lines to enable the admin:
if settings.DEBUG or settings.FEATURES.get('ENABLE_DJANGO_ADMIN_SITE'):
    admin.autodiscover()

# Use urlpatterns formatted as within the Django docs with first parameter "stuck" to the open parenthesis
urlpatterns = (
    url(r'^document/', 'lacviet.document.views.get_document'),
    url(r'^wiki$', 'lacviet.wiki.views.get_wiki'),
    url(r'^exam$', 'lacviet.exam.views.get_exam'),
    url(r'^survey$', 'lacviet.survey.views.get_survey'),
)
