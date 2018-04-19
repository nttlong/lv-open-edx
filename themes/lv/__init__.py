import lv_utils
import uuid

from contentstore.views.course import create_new_course_in_store
from xmodule.modulestore.django import modulestore
from util.string_utils import _has_non_ascii_characters
from util.organizations_helpers import add_organization_course, get_organization_by_short_name, organizations_enabled
from django.conf import settings
from xmodule.course_module import DEFAULT_START_DATE, CourseFields
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.http import *

"function API: Create token with a user"
"Method: POST"
"Parameter:username"
def get_user_db(param):
    #get param from request
    #Check username exist in db if exist then update token of user
    try:
        if User.objects.filter(username=param["username"]).exists():
            token = str(uuid.uuid4())
            user_lg = lv_utils.mongo_db()["hcs_users"].update_one({"username":param["username"]},{"$set": {
                "token":token
            }})
            return {
                "username": param["username"],
                "token": token
            };
        #if not exist in db then create user in db
        else:
            #Create password in 2 bb mongodb and mysql
            passwd = str(uuid.uuid4())
            user_lg = {
                "username": param["username"],
                "token" : str(uuid.uuid4()),
                "password": passwd
            }
            #insert in db mongodb
            lv_utils.mongo_db()["hcs_users"].insert_one(user_lg)
            #insert in db mysql
            userInsert = User.objects.create_user(param["username"], param["email"], passwd)

            userInsert.save()
            return {
                "username": user_lg["username"],
                "token": user_lg["token"]
            };
    except Exception as error:
        return {
            "error": error
        }

"function API: Insert database a course"
"Parameter org, course, display_name, codeteacher"
"Method: POST"
def create_course_manage(param):
    try:
        #get param from request
        org = param['org']
        course = param['course']
        display_name = param['display_name']
        # force the start date for reruns and allow us to override start via the client
        start =  CourseFields.start.default
        run = param['run']
        codeteach = param['codeteacher']

        # allow/disable unicode characters in course_id according to settings
        if not settings.FEATURES.get('ALLOW_UNICODE_COURSE_ID'):
            if _has_non_ascii_characters(org) or _has_non_ascii_characters(course) or _has_non_ascii_characters(run):
                return JsonResponse(
                    {'error': _('Special characters not allowed in organization, course number, and course run.')},
                    status=400
                )

        fields = {'start': start}
        if display_name is not None:
            fields['display_name'] = display_name

        # Set a unique wiki_slug for newly created courses. To maintain active wiki_slugs for
        # existing xml courses this cannot be changed in CourseDescriptor.
        # # TODO get rid of defining wiki slug in this org/course/run specific way and reconcile
        # w/ xmodule.course_module.CourseDescriptor.__init__
        wiki_slug = u"{0}.{1}.{2}".format(org, course, run)
        definition_data = {'wiki_slug': wiki_slug}
        fields.update(definition_data)
        user_test = User.objects.filter(username=codeteach).first()

        org_data = get_organization_by_short_name(org)
        if not org_data and organizations_enabled():
            return JsonResponse(
                {'error': _('You must link this course to an organization in order to continue. '
                            'Organization you selected does not exist in the system, '
                            'you will need to add it to the system')},
                status=400
            )
        store_for_new_course = modulestore().default_modulestore.get_modulestore_type()
        new_course = create_new_course_in_store(store_for_new_course, user_test, org, course, run, fields)

        add_organization_course(org_data, new_course.id)

        return {
            "data": new_course,
            "error": None
        }
    except Exception as error:
        return {
            "data": error,
            "error": True
        }