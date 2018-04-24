# -*- coding: utf-8 -*-
import quicky
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
app=quicky.applications.get_app_by_file(__file__)
import json
@quicky.view.template("index.html")
def index(request):
    return request.render(dict(
        menu_items=app.settings.menu_items
    ))
@quicky.view.template("dynamic.html")
def load_page(request,path):

    return request.render({
        "path": path.lower()
    })
@require_http_methods(["POST"])
@csrf_exempt
def api(request):
    setattr(request,"app",app)
    ret_data=quicky.caller.call(request)
    return HttpResponse(ret_data)