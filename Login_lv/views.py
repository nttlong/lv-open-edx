from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.http import *
import lv_utils
from lv_utils import configs
__cache__authenticate={}

"API function: sigin system with token"
"Method: POST"
"Parameter: token, next link"
def signin(request):
    token=None
    next = None
    #userInsert = User.objects.create_user("user001", "user001@gmail.com", "user001")
    #userInsert.is_staff = 1
    #userInsert.save()
    #check token have request
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
        __cache__authenticate.update({token:{
            "hcs_user":user_lg,
            "user":user
        }})
        if user is not None:
            login(request, user)
            if next != None:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(configs.get_host_url()+"/courses")
    else:
        return HttpResponseRedirect(configs.get_host_url()+"/static/error.html")