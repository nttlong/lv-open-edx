from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.http import *
import lv_utils
from lv_utils import configs
def signin(request):
    token=None
    next = None
    if (request._get_request().has_key("token")):
        token = request.GET["token"]
    else:
        if(request._get_request().has_key("next")):
            return HttpResponseRedirect(configs.get_login_url() + "?source=open-edx&next="+request.GET["next"])
        else:
            return HttpResponseRedirect(configs.get_login_url() + "?source=open-edx")

    if(request._get_request().has_key("next")):
        next=request.GET["next"]
    user_lg = lv_utils.mongo_db()["hcs_users"].find_one({"token": token})
    if user_lg != None:
        user = authenticate(username=user_lg["username"], password=user_lg["password"])
        if user is not None:
            login(request, user)
            if next != None:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(configs.get_host_url()+"/courses")
    else:
        return HttpResponseRedirect(configs.get_host_url()+"/static/error.html")
