import forms
from courseware.courses import get_course_about_section
from language_resource import resources
def debug(request,data):
    print data
def helper(request):
    return resources(request)


