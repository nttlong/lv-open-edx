from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
import  importlib
@require_http_methods(["POST"])
@csrf_exempt
def web_services(request):
    post_data=json.loads(request.body)



    if(post_data.get("path")==None):
        HttpResponse(json.dumps({
            "error":"true",
            "message":"path was not set. The 'path' must be {module_name}@{method_name}"
        }), content_type="application/json")
        return
    if(post_data.get("path").split("@").__len__()!=2):
        HttpResponse(json.dumps({
            "error": "true",
            "message": "Invalid 'path'. The 'path' must be {module_name}@{method_name}"
        }), content_type="application/json")
        return
    module_name=post_data.get("path").split("@")[0]
    method_name=post_data.get("path").split("@")[1]

    mdl=importlib.import_module(module_name)
    if(mdl==None):
        HttpResponse(json.dumps({
            "error": "true",
            "message": "'"+module_name+"' was not found"
        }), content_type="application/json")
        return
    fn=getattr(mdl,method_name)
    if(fn==None):
        HttpResponse(json.dumps({
            "error": "true",
            "message": "'" + method_name + "' was not found in '"+module_name+"'"
        }), content_type="application/json")
        return
    retData={}
    if(post_data.get("params")!=None):
        retData=fn(json.loads(post_data.get("params")))
    else:
        retData=fn()
    return HttpResponse(json.dumps(retData), content_type="application/json")